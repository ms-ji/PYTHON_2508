import logging


def main():
    """
    
    """
    # 기본 설정

    logging.basicConfig(filename='PCWK_log.log',level=logging.INFO,
                        format='%(asctime)s[%(levelname)s] %(filename)s %(lineno)d %(message)s',
                        datefmt='%y-%m-%d %H:%M:%S')

    # 로그 메시지 출력
    logging.debug('debug 메시지')
    logging.info('debug 메시지')
    logging.warning('debug 메시지')
    logging.error('debug 메시지')
    logging.critical('debug 메시지')


if __name__ == '__main__':
    main()
