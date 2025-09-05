def order(item,quantity =1,price=1000):
    total = quantity * price
    print(f'{quantity}개 {item}: {total}원')

order('수박맛 바',quantity=3)
order('메론',price=2000)

# 3개 수박맛 바: 3000원
# 1개 메론: 2000원
