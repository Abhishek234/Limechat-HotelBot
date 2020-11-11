
## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- hi again
- hi there

## intent:thank
- Thanks
- Thank you
- Thank you so much
- Thanks 
- Thanks for that

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:name
- My name is [Tatiana](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- My name is [John](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I am [Philipp](name)
- I am [Charlie](name)




## intent:book room
-I wish to book a [room](location) in your hotel
-I want to book a [single room](location) in your hotel
-I want to book a [deluxe room](location) in your hotel 
=I want to book a[room](location)
-I would like to book a [room](location) 
-Could you please help me to book a [room](location)in your hotel
- Please book a [room](location)
- Book a [room](location)
- Please help me book a [room](location)
-Please book [rooms](location)

## intent:book no of room
- I wish to book (1)[number] [rooms](location) 
- I wish to book (2)[number] [rooms](location)
- Please book me a (single)[number] [room](location)
- Please book me a (two)[number] [room](location)
- book (1)[number] [rooms] (location)
- book (2)[number] [rooms] (locaiton)
-
## intent:num_rooms
- [1](number)
- [2](number)

## intent:type_rooms
- [Simple](room_type)
- [Deluxe](room_type)

## intent:clean_room
- I need someone to clean the [room](location)?
- Please ask somone to clean room [room](location) clean
- Room cleaning[room](location) 
- i want to have my [room](location) cleaned
## intent:clean_room_now
- now
-its urgent
- send someon right now
- room cleaning service right now
## intent:clean_room_later
-send someone to clean the room after (3)[hours](time)
- please send someone to clean the room after (3)[hours](time)
-room cleaning service needed after (2)[hours](time)

## intent:faq_check_in_time
- What is the check in time at your hotel?
- what are the check in timings
- I want to know about the check in timings
- When can I check in at your location?
## intent:faq_check_out_time
- What is the check outtime at your hotel?
- what are the check out timings
- I want to know about the check out timings
- When can I check out at your location?

## intent:faq_cancel_reservation
- How can I cancel my booking?
- How can I cancel the reservation that I did?
- How can I cancel the resrvation
- Let me know how can I cancel my bookings

## intent:faq_cancellation_policy
- i want to know about the cancellation policy
- I would like to know about the cancellation policy
- what is the cancellation policy 
- I want to enquire about the cancellation policy

## intent:faq_refund_policy
- i want to know about the refund policy
- I would like to know about the refund policy
- what is the refund policy 
- I want to enquire about the refund policy

## intent:faq_have_restaurant
- Can you tell me about the restaurants available
- What are the restaurants available at your location
-I want to know about the restaurants available
- Does your hotel have restaurant

## intent:faq_breakfast_avail
-does the hotel offer breakfast 
- what is the breakfast service available at your hotel
- is the breakfast available at the restaurant 
- what are the breakfast options available
- what are the breakfast options available at the hotel 
