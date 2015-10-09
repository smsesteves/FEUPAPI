__author__ = 'smsesteves'

import requests
import xml.etree.ElementTree as ET

class RoomSchedule():
    ID_POLO = 164

    def get_room_schedule(self,room):
        return room

    def is_valid(self,room):
        return True

    def get_room_id(self,room_name):
        jsondata = {
            "pv_sigla":room_name,
            "pv_polo": self.ID_POLO,
            "pv_activo":"S"
        }
        r = requests.post("https://sigarra.up.pt/feup/pt/instal_geral.espaco_list",data=jsondata)
        #print(r.text)
        #tree = ET.fromstring(r.text)
        #root = tree.getroot()
        #print(root.tag)
        return "73201"