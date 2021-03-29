exemplo para explicação do checksum

MENSAGEM 1  MENSAGEM 2  MENSAGEM 3 
101010101   110101010   100000000

TRANSCEIVER                                     RECEIVER 
						                                    MENSAGEM 1   MENSAGEM 2  MENSAGEM 3   EDC 
SOMA MSG1 + MSG2				                        101010101    110101010   100000000    111111110
 101010101
+110101010
------------------------                         
 011111111  OVERFLOW                            
+000000001
------------------------
 100000000 (MSG1 + MSG2)
+100000000 (MSG3)
------------------------
 000000000 OVERFLOW
+000000001
------------------------
 000000001  RESULTADO DA SOMA
 111111110  EDC
