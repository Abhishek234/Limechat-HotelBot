
from typing import List,Dict,Text,Any,Union
From rasa import nlu
from rasa_sdk import Actions,tracker
from rasa_sdk_events  import Slotset, UserUtteranceReverted
from rasa_sdk_executor import CollectingDispatcher
from rasa_sdk_forms import FormAction


def repeat(tracker, dispatcher):
    user_ignore_count = 2
    count = 0
    tracker_list = []

    while user_ignore_count > 0:
        event = tracker.events[count].get('event')
        if event == 'user':
            user_ignore_count = user_ignore_count - 1
        if event == 'bot':
            tracker_list.append(tracker.events[count])
        count = count - 1

    tracker_list.reverse()
    i = len(tracker_list) - 1

    while i >= 0:
        data = tracker_list[i].get('data')
        if data:
            if "buttons" in data:
                dispatcher.utter_message(text=tracker_list[i].get('text'), buttons=data["buttons"])
            else:
                dispatcher.utter_message(text=tracker_list[i].get('text'))
            break
        i -= 1



class HotelForm(FormAction):
    #Assume the form to be filled at reception

    def name(self)-> Text:
        return "form_book_room"

    @staticmethod
    def required_slots(tracker)-> List[Text]:
        return ["number","room_type"]
    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[text,Any] ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit", number=tracker.get_slot('number'),room_type=tracker.get_slot('room_type'))


    
    def slot_mappings(self)->Dict[Text,Union[Dict,List[Dict]]]:
        # We are creating a dictionary which is required to map an enity, mesesgae and the intent
        return{
            "number":self.from_entity(entity="number",intent="num_rooms")
            "room_type":self.from_entity(entity="room_type",intent="type_rooms")
            "phone_number":self.from_entity(entity="number ",intent="contact")
        }
class BookRoomNumber(FormAction):
    def name(self)-> Text:
        return "form_book_room_number"
    @staticmethod
    def required_slots(tracker)-> List[Text]:
        return ["number","room_type"]
    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[text,Any] )-> List[Dict]:
        dispatcher.utter_message(template="utter_submit", number=tracker.get_slot('number'),room_type=tracker.get_slot('room_type'))


    def slot_mappings(self)->Dict[Text,Union[Dict,List[Dict]]]:
        # We are creating a dictionary which is required to map an enity, mesesgae and the intent
        return{
            "room_type":self.from_entity(entity="room_type",intent="type_rooms")
             }

    class RecentSlot(Action):
        def name(self):
            return "action_reset_slots"
        def run(self, dispatcher, tracker, domain):
        return [SlotSet("number", None), SlotSet("room_type", None)]
    
    class FallbackAction(Action):
        def name(self):
            return "action_fallback"
        def run(self, dispatcher, tracker, domain):
             dispatcher.utter_template("utter_fallback_message", tracker)
             return [UserUtteranceReverted()]
             
            
        #dispatcher.utter_template("utter_fallback_message", tracker)
        # repeat(tracker, dispatcher)        
        #return [UserUtteranceReverted()]

    class ActionCheckinTIme(Action):
        def name(self):
            return "action_check_in_time"

        

        def run(self, dispatcher, tracker, domain):
            dispatcher.utter_template("utter_check_in_time", tracker)
            repeat(tracker, dispatcher)
            return [UserUtteranceReverted()]

    class ActionCheckoutTIme(Action):
        def name(self):
            return "action_check_out_time"
        def run(self, dispatcher, tracker, domain):
            dispatcher.utter_template("utter_check_out_time",tracker)
            repeat(tracker,dispatcher)
            return(UserUtteranceReverted)

    class ActionCancelReservation(Action):
        def name(Self):
            return "action_cancel_reservation"
    
        def run(self, dispatcher, tracker, domain):  
            dispatcher.utter_template("utter_cancel_reservation", tracker)
            repeat(tracker,dispatcher)
            return(UserUtteranceReverted)


    class ActionCancellationPolicy(Action):

        def name(self):
            return "action_cancellation_policy"

        def run(self, dispatcher, tracker, domain):
            dispatcher.utter_template("utter_cancellation_policy",tracker)
            repeat(tracker,dispatcher)
            return(UserUtteranceReverted)

    class ActionRefundPolicy(Action):
        def name(self):
            return "action_refund_policy"
        
        def run(self,dispatcher,tracker,domain):
            dispatcher.utter_template("utter_refund_policy",tracker)
            repeat(tracker,dispatcher)
            return(UserUtteranceReverted)
        
    class ActionHaveRestaurant(Action):
        def name(Self):
            return "action_have_restaurant"
        
        def run(self,dispatcher,template,domain):
            dispatcher.utter_template("utter_have_restauant",tracker)
            return(tracker,dispatcher)
            return(UserUtteranceReverted)
    
    class ActionAvailBreakfast(Action):
        def name (self):
            return "utter_avail_breakfast"
        
        def run(self, dispatcher,template,domain):
            dispatcher.utter_template("utter_avail_breakdfast",tracker)
            return(tracker,dispatcher)
            return(UserUtteranceReverted)
        
    class ActionRestaurantTime(Action):
        def name(self):
            return "utter_restaurant_time"
        
        def run(self,dispatcher,template,domain):
            dispatcher.utter_template("utter_restaurant_time",tracker)
            return(tracker,dispatcher)
            return(UserUtteranceReverted)
