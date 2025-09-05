from mypackage.p_log import logger as log

def main():
    """
    
    """
    # 로그 메시지 출력
    log.debug('debug99 메시지')
    log.info('debug99 메시지')
    log.warning('debug99 메시지')
    log.error('debug99 메시지')
    log.critical('debug99 메시지')

if __name__ == '__main__':
    main()
