## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 ## confirm room book- ask the user about the no of rooms and type of tooms
 * greet
    -utter_greet
   book_room{"location_room":"location"}
    - book_room_form
    - form {"name":"book_room_form"}
    - foom {"name":null}
    - action_reset_slots
    - utter_is_that_all
   
*  affirm
    -utter_bye
## deny room book 
* greet
  - utter_greet
* book_room{"location":"room"}
  - form_book_room
  - form{"name": "form_book_room"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* deny
  - utter_deny_message

## book number room affirm 1 
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"1"}
  - slot{"number": "1"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* affirm
  - utter_goodbye

## book number room deny 1 
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"1"}
  - slot{"number": "1"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* deny
  - utter_deny_message

## book number room affirm 2
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"2"}
  - slot{"number": "2"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* affirm
  - utter_goodbye

## book number room deny 2
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"2"}
  - slot{"number": "2"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* deny
  - utter_deny_message

## clean room now affirm
* greet
  - utter_greet
* clean_room{"location":"room"}
  - utter_clean_room
* clean_room_now
  - utter_clean_room_now
  - utter_is_that_all
* affirm
  - utter_goodbye

## clean room now deny
* greet
  - utter_greet
* clean_room{"location":"room"}
  - utter_clean_room
* clean_room_now
  - utter_clean_room_now
  - utter_is_that_all
* deny
  - utter_deny_message

## clean room later affirm
* greet
  - utter_greet
* clean_room{"location":"room"}
  - utter_clean_room
* clean_room_relative
  - utter_clean_room_relative
  - utter_is_that_all
* affirm
  - utter_goodbye
## faq check in time affirm
* greet
  - utter_greet
* faq_check_in_time
  - utter_check_in_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq check in time deny
* greet
  - utter_greet
* faq_check_in_time
  - utter_check_in_time
  - utter_is_that_all
* deny
  - utter_deny_message

## faq check out time affirm
* greet
  - utter_greet
* faq_check_out_time
  - utter_check_out_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq check out time deny
* greet
  - utter_greet
* faq_check_out_time
  - utter_check_out_time
  - utter_is_that_all
* deny
  - utter_deny_message

## faq cancel reservation affirm
* greet
  - utter_greet
* faq_cancel_reservation
  - utter_cancel_reservation
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq cancel reservation deny
* greet
  - utter_greet
* faq_cancel_reservation
  - utter_cancel_reservation
  - utter_is_that_all
* deny
  - utter_deny_message

## faq cancellation policy affirm
* greet
  - utter_greet
* faq_cancellation_policy
  - utter_cancellation_policy
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq cancellation policy deny
* greet
  - utter_greet
* faq_cancellation_policy
  - utter_cancellation_policy
  - utter_is_that_all
* deny
  - utter_deny_message

## faq have restaurant affirm
* greet
  - utter_greet
* faq_have_restaurant{"location": "restaurant"} 
  - utter_have_restaurant
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq have restaurant deny
* greet
  - utter_greet
* faq_have_restaurant{"location": "restaurant"} 
  - utter_have_restaurant
  - utter_is_that_all
* deny
  - utter_deny_message

## faq breakfast availability affirm
* greet
  - utter_greet
* faq_breakfast_avail
  - utter_breakfast_avail
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq breakfast availability deny
* greet
  - utter_greet
* faq_breakfast_avail
  - utter_breakfast_avail
  - utter_is_that_all
* deny
  - utter_deny_message

## faq breakfast time affirm
* greet
  - utter_greet
* faq_breakfast_time
  - utter_breakfast_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq breakfast time deny
* greet
  - utter_greet
* faq_breakfast_time
  - utter_breakfast_time
  - utter_is_that_all
* deny
  - utter_deny_message

## faq restaurant time path affirm
* greet
  - utter_greet
* faq_restaurant_time{"location": "restaurant"}
  - utter_restaurant_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq restaurant time deny
* greet
  - utter_greet
* faq_restaurant_time{"location": "restaurant"}
  - utter_restaurant_time
  - utter_is_that_all
* deny
  - utter_deny_message
## story_name



* name{"name":"Sam"}
 - utter_greet

## story_joke_01
* joke
 - action_joke
 
## story_order_product
* order_product{"product":"laptop"}
 - utter_ask_model_name
* order_model{"model":"MacBook"}
 - utter_place_order
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 

## story_thanks
* thanks
 - utter_thanks

## story_goodbye
* goodbye
 - utter_goodbye