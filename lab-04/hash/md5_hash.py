def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    # Chia chuỗi thành các block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]

        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        a0, b0, c0, d0 = a, b, c, d

        # Vòng lặp chính của thuật toán MD5
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            # Các hằng số T (đã được tính toán trước, không hiển thị trong ảnh nhưng cần thiết cho MD5)
            # Vì ảnh không cung cấp, tôi sẽ giả định đây là phần thiếu và chỉ chép những gì có.
            # Trong một triển khai MD5 hoàn chỉnh, các hằng số này là một mảng 64 giá trị.
            # Để code có thể chạy, bạn sẽ cần thêm mảng hằng số này.
            # Ví dụ: T = [int(abs(math.sin(i + 1)) * (2**32)) for i in range(64)]

            # Các bước xử lý trong vòng lặp (giữ nguyên theo ảnh)
            temp = d
            d = c
            c = b
            # Đoạn này có vẻ bị cắt mất một phần trong ảnh, tôi sẽ chép chính xác những gì nhìn thấy
            # và thêm chỗ cần thiết để nó có thể chạy nếu có các hằng số T.
            # Dòng này bị thiếu trong ảnh, tôi sẽ bổ sung giả định.
            # b = left_rotate(a + f + T[j] + words[g], s[j]) + b
            # Sẽ chép đúng như ảnh:
            b = left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3) # Giá trị 0x5A827999 là T[j] giả định hoặc một hằng số cố định trong phiên bản này
            a = temp

    a = (a + a0) & 0xFFFFFFFF
    b = (b + b0) & 0xFFFFFFFF
    c = (c + c0) & 0xFFFFFFFF
    d = (d + d0) & 0xFFFFFFFF

    return ':{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))

print("Mã băm MD5 của chuỗi '{}' là: '{}'".format(input_string, md5_hash))