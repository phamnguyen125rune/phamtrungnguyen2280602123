def xoa_phan_tư(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

#sử dụng hàm và in kết quả
my_dict = {'a': 1, 'b': 2, 'c':3, 'd': 4}
key_to_delete = 'b'
result = xoa_phan_tư(my_dict, key_to_delete)
if result == True:
    print("Phần tử đã được xóa: ", my_dict)
else:
    print("Không tồn tại phần tử cần xóa trong dictionary, ", my_dict)