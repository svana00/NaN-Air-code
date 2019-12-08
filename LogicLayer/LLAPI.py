from LogicLayer.StaffMemberLL import StaffMemberLL
from LogicLayer.VoyageLL import VoyageLL
from LogicLayer.AirplaneLL import AirplaneLL
from LogicLayer.DestinationLL import DestinationLL
from DataLayer.IOAPI import IOAPI

class LLAPI():

    def __init__(self):
        self.ioAPI = IOAPI()
        self.destLL = DestinationLL(self.ioAPI)
        self.staffLL = StaffMemberLL(self.ioAPI)
        self.voyageLL = VoyageLL(self.ioAPI)
        self.airplaneLL = AirplaneLL(self.ioAPI)

    def get_staff_member_info(self, ssn):
        return self.staffLL.get_staff_member_info(ssn)

    def get_all_airplane_types(self):
        return self.staffLL.get_all_airplane_types()

    def get_pilots_by_one_licence(self,airplane_type_id):
        return self.staffLL.get_pilots_by_one_licence(airplane_type_id)

    def get_pilots_by_all_licences(self):
        return self.staffLL.get_pilots_by_all_licences()

    def get_all_staff(self):
        return self.staffLL.get_all_staff()

    def get_destinations(self):
        return self.destLL.get_destinations()

    def get_destination_info(self, dest_id):
        return self.destLL.get_destination_info(dest_id)

    def get_mutable_destination_info_list(self):
        return self.destLL.get_mutable_destination_info_list()

    def create_new_destination(self, dest_list):
        self.dest_list = dest_list
        return self.destLL.create_new_destination(self.dest_list)

    def get_all_pilots(self):
        return self.staffLL.get_all_pilots()

    def get_all_flight_attendants(self):
        return self.staffLL.get_all_flight_attendants()

    def create_staff_member(self, staff_member_info_list):
        return self.staffLL.create_staff_member(staff_member_info_list)

    def get_all_voyages(self):
        hardkodadur_listi_sem_eg_mun_eyda = [["NA5614","KEF","LYR","2019-11-02T06:21:00","2019-11-02T10:21:00","TF-KOR","3009907461","2410876598","1600904199","3002688722","0505942924","NA7299","LYR","KEF","2019-11-02T11:21:00,2019-11-02T15:21:00","TF-KOR","3009907461","2410876598","1600904199","3002688722","0505942924"], [" NA2551" ,"KEF","LYR,2019-11-04T05:32:00","2019-11-04T09:32:00","TF-HLB","2910858778","2211658134","0303758167","3003962187","1110732819","NA5675","LYR","KEF","2019-11-04T10:32:00","2019-11-04T14:32:00","TF-HLB","2910858778","2211658134","0303758167","3003962187","1110732819"]]
        return hardkodadur_listi_sem_eg_mun_eyda

    def create_new_airplane(self, airplane_str):
        self.airplane_str = airplane_str
        return self.airplaneLL.makeAirplane(airplane_str)

    def get_all_working(self, departure_out_date):
        return self.staffLL.get_all_working(departure_out_date)

    def get_all_not_working(self, departure_out_date):
        return self.staffLL.get_all_working(departure_out_date)