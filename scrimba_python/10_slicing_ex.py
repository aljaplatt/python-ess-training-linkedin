msg='welcome to Python 101: Strings'
  
print(msg)

print(f"1 {msg[:7]} {msg[25:29]} to tyler".title()[::-1])
# msg_backwards = f"1 {msg[:7]} {msg[25:29]} to tyler".title()
# print(msg_backwards[::-1])

msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
print(msg1[::-1])