"""Running the Xetra ETL application"""
import logging # quelle est l interet d importer logging.config si on a dèja importé logging en entier 
import logging.config

import yaml

def  main():
    """ Entry point to run the xetra ETL job """
    
    #Parsing YAML file
    
    config_path='./configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))   #yaml.safe_load() convertit le contenu du fichier en une structure de données Python. Cette structure peut être un dictionnaire, une liste, etc., selon le contenu du fichier YAML.
    #print(config)
    log_config = config['logging']
    logging.config.dictConfig(log_config) #configure le système de logging de Python en utilisant la configuration chargée à partir du fichier YAML. La fonction dictConfig() de logging.config prend un dictionnaire Python contenant la configuration du logging et l'applique au système de logging.
    logger = logging.getLogger(__name__)
    logger.info("This is a test") #Cette ligne utilise le logger pour enregistrer un message d'information.
    


if __name__ == '__main__': #vérifie si le script est exécuté en tant que programme principal
    main()
    