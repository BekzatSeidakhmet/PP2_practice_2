import json
from connect import get_connection


def add_contact(name, email, birthday):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO contacts(name, email, birthday)
        VALUES (%s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (name, email, birthday))

    conn.commit()
    cur.close()
    conn.close()


def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = cur.fetchall()

    contacts = {}

    for row in data:
        name, email, birthday, group, phone, ptype = row

        if name not in contacts:
            contacts[name] = {
                "email": email,
                "birthday": str(birthday),
                "group": group,
                "phones": []
            }

        if phone:
            contacts[name]["phones"].append({
                "number": phone,
                "type": ptype
            })

    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

    cur.close()
    conn.close()


def import_json():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for name, info in data.items():

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists. skip/overwrite: ")

            if choice == "skip":
                continue
            elif choice == "overwrite":
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("""
            INSERT INTO contacts(name, email, birthday)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (name, info["email"], info["birthday"]))

        cid = cur.fetchone()[0]

        for p in info["phones"]:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (cid, p["number"], p["type"]))

    conn.commit()
    cur.close()
    conn.close()


def filter_by_group(group):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def search_email(email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT name, email FROM contacts
        WHERE email ILIKE %s
    """, ('%' + email + '%',))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def paginate(limit=5):
    conn = get_connection()
    cur = conn.cursor()

    offset = 0

    while True:
        cur.execute("""
            SELECT name FROM contacts
            ORDER BY name
            LIMIT %s OFFSET %s
        """, (limit, offset))

        rows = cur.fetchall()

        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break

    cur.close()
    conn.close()


def main():
    while True:
        print("""
1 Add contact
2 Export JSON
3 Import JSON
4 Filter by group
5 Search email
6 Pagination
0 Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            birthday = input("Birthday YYYY-MM-DD: ")
            add_contact(name, email, birthday)

        elif choice == "2":
            export_json()

        elif choice == "3":
            import_json()

        elif choice == "4":
            group = input("Group: ")
            filter_by_group(group)

        elif choice == "5":
            email = input("Email search: ")
            search_email(email)

        elif choice == "6":
            paginate()

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
