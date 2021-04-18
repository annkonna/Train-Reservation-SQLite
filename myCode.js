
function bookingsCallback(response){
    var bookings = JSON.parse(response);
    console.log(bookings);
    var to_html = "";
    for(var train_no in bookings){
        var booking = bookings[train_no];
//        booking.train_no
//        bookin.seat_no
//        booking.pass_name
        to_html = to_html + booking.train_no + " - " + booking.seat_no + " - " + booking.pass_name + "</a><br/>";
        
        to_html = to_html + "<hr/>";
    }
    console.log(to_html);
    document.getElementById("bookings").innerHTML = to_html;
}

function getBookings(){
    ajaxGetRequest("bookings", bookingsCallback);
}


function newBooking(){
    train_no = document.getElementById("train_no_input").value;
    seat_no = document.getElementById("seat_no_input").value;
    pass_name = document.getElementById("pass_name_input").value;
    
    document.getElementById("train_no_input").value = "";
    document.getElementById("seat_no_input").value = "";
    document.getElementById("pass_name_input").value = "";
    
    booking = {"train_no": train_no, "seat_no": seat_no, "pass_name": pass_name};
    booking = JSON.stringify(booking);
    console.log(booking);
    ajaxPostRequest("add_booking", booking, bookingsCallback)
}


function ajaxGetRequest(path, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}


function ajaxPostRequest(path, data, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}
