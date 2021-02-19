def sum_two_large_numbers(str1,str2):
  str1_len = len(str1)-1;
  str2_len = len(str2)-1;

  result="";

  carry =0;

  while str1_len >= 0 or str2_len >=0:
  
    #ternary operator: a if condition else b
  
    digit1 = (ord(str1[str1_len]) - 48) if str1_len > -1 else 0;
    digit2 = (ord(str2[str2_len]) - 48) if str2_len > -1 else 0;
  
    sum = digit1 + digit2 + carry;
  
    add = int(sum%10);
  
    result += str(add);
  
    carry = int(sum / 10);
  
    str1_len -= 1;
    str2_len -= 1;

  if carry!=0:
    result += str(carry);


  return result[::-1];

