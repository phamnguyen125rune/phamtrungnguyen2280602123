from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId = 1
        if(self. soLuongSinhVien()> 0):
            maxId = self.listSinhVien[0]._id 
            for sv in self.listSinhVien:
                if(maxId <sv._id):
                    maxId=sv._id 
            maxId = maxId + 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.", format(ID))
            
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse = False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse = False)
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse = False)
    def findByID(self, ID):
        s = None
        if (self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                     s = sv
        return s
    def findByName(self, keyword):
        listSV= []
        if(self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self, ID):
        isDelete = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDelete = True
        return isDelete

            