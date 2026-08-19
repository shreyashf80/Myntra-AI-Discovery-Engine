import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.shared.db import get_connection, init_db, mark_items_processed, delete_raw_batch

def migrate():
    print("Initializing DB to ensure new table exists...")
    init_db()
    
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM tagged_items")
    rows = c.fetchall()
    conn.close()
    
    tagged_ids = [r['id'] for r in rows]
    print(f"Found {len(tagged_ids)} items in tagged_items.")
    
    if tagged_ids:
        print("Marking items as TAGGED in processed_items ledger...")
        mark_items_processed(tagged_ids, 'TAGGED')
        print("Purging these items from raw_items queue...")
        delete_raw_batch(tagged_ids)
        
    print("Migration complete!")

if __name__ == "__main__":
    migrate()
