C PORT OF C++ CODE IN FORTRAN 77, FOR FUN...

      INTEGER FUNCTION FPOW(F, P)
          INTEGER F, P, X
          FPOW = 0
          X = P

          DO WHILE (F .GE. X)
              FPOW = FPOW + F / X
              X = X * P
          ENDDO
          RETURN
      END

      PROGRAM P154
      INTEGER I, J, K, C, FPOW, IJK2, IJK5
      INTEGER FPOW2(0:200000), FPOW5(0:200000)

      DO I = 0, 200000
         FPOW2(I) = FPOW(I, 2)
         FPOW5(I) = FPOW(I, 5)
      ENDDO

      C = 0
      DO I = 0, 200000/3
          DO J = I, (200000-I)/2
              K = 200000 - I - J
              IJK2 = FPOW2(I) + FPOW2(J) + FPOW2(K)
              IJK5 = FPOW5(I) + FPOW5(J) + FPOW5(K)
              IF ((FPOW2(200000) - IJK2 .GE. 12) .AND. 
     +            (FPOW5(200000) - IJK5 .GE. 12)) THEN
                  IF ((I.EQ.J .AND. J.LT.K) .OR. 
     +                (I.LT.J .AND. J.EQ.K)) THEN 
                      C = C + 3
                  ELSE 
                      C = C + 6       
                  ENDIF
              ENDIF
          ENDDO
      ENDDO

      WRITE(*,*) C
      STOP
      END
