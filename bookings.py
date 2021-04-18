import sqlite3

# START UP WORK

conn = sqlite3.connect("bookings.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS 'bookings' ('train_no', 'seat_no', 'pass_name')")


def allBookings():
    return cur.execute("SELECT * FROM bookings")


def insertBooking(booking):
    cur.execute('INSERT INTO bookings VALUES (?,?,?)', (booking['train_no'], booking['seat_no'], booking['pass_name']))


def bookingIDAlreadyExists(train_no, seat_no):
    for row in cur.execute("SELECT * FROM bookings WHERE train_no=? and seat_no=?", (train_no, seat_no)):
        return True
    return False


def get_bookings():
    bookingDict = {}
    for row in allBookings():
        train_no = row[0]
        seat_no = row[1]
        pass_name = row[2]
        bookingDict[train_no + seat_no] = {"train_no": train_no, "seat_no": seat_no, "pass_name": pass_name}
    return bookingDict


def bookingNotValid(booking):
    return 'train_no' not in booking or 'seat_no' not in booking or 'pass_name' not in booking or booking[
        'train_no'] == "" or booking['seat_no'] == "" or booking['pass_name'] == ""


def add_booking(booking):
    if bookingNotValid(booking) or bookingIDAlreadyExists(booking['train_no'], booking['seat_no']):
        return
    insertBooking(booking)
    conn.commit()
