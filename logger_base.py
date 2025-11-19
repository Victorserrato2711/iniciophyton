import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers = [
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug(f'Mensaje a Nivel de Bug')
    log.info(f'Mensaje a Nivel de Info')
    log.warning(f'Mensaje a Nivel de warning')
    log.error(f'Mesaje a nivel de Error')
    log.critical(f'Mensaje a Nivel Critical')