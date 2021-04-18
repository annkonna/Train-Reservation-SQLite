import sqlite3
import bookings

booking = {'train_no':'12345678902', 'seat_no': '9D', 'pass_name' : 'Ann Gina Mathew'}
bookings.add_booking(booking)
for entry in bookings.allBookings():
    print(entry)
print(bookings.bookingIDAlreadyExists('12345678901','8D'))
print(bookings.bookingIDAlreadyExists('1234567890', '9D'))
boking = {'train_no':'12345678901', 'seat_no': '8D', 'pass_name' : 'Ann Sheryl Mathew'}
bookings.insertBooking(boking)
print(bookings.get_bookings())
