import csv


def main():
    """
    
    """
def write_csv(filename,data):
    '''
    csv  파일 생성
    :param filename:
    :param data:
    :return: void
    '''
    with open(filename,'w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)

        #header
        writer.writerow(['이름','나이','취미'])
        #data
        writer.writerows(data)

        '''
        이상무,22,독서
        영희,18,Cycling
        철수,21,게임
        '''
# 호출
write_csv('csv_data.csv', [
    ['이상무', 22, '독서'],
    ['영희', 18, 'Cycling'],
    ['철수', 21, '게임']
])

def read_csv(filename):
    '''
    csv 읽기
    :param filename:
    :return: void
    '''
    with open('score_data.csv','r',encoding='utf-8') as file:
        reader = csv.DictReader(file)


        for row in reader:
            name = row['이름']
            tmp_list = [ int(row['국어']),int(row['영어']),int(row['수학'])]
            #print(type(int(row['국어'])))
            avg = sum(tmp_list)/len(tmp_list)

            print(f'{name}의 평균은 {avg:.2f}입니다.')

read_csv('csv_data.csv')

if __name__ == '__main__':
    main()
