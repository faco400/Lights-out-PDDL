(define (problem p01-10x10)
  (:domain lightsout)
  (:objects
    x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 y0 y1 y2 y3 y4 y5 y6 y7 y8 y9 - cell
  )
  (:init
    ; Definir as relações de adjacência para a matriz 10x10
    (inc x0 x1) (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6) (inc x6 x7) (inc x7 x8) (inc x8 x9)
    (inc y0 y1) (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6) (inc y6 y7) (inc y7 y8) (inc y8 y9)
    (dec x9 x8) (dec x8 x7) (dec x7 x6) (dec x6 x5) (dec x5 x4) (dec x4 x3) (dec x3 x2) (dec x2 x1) (dec x1 x0)
    (dec y9 y8) (dec y8 y7) (dec y7 y6) (dec y6 y5) (dec y5 y4) (dec y4 y3) (dec y3 y2) (dec y2 y1) (dec y1 y0)

    ; Definir o estado inicial com luzes ligadas, desligadas e quebradas
    (light-on x0 y2) (light-on x0 y3) (light-on x0 y4) (light-on x1 y3) (light-on x1 y4)
    (light-on x2 y0) (light-on x2 y3) (light-on x2 y4) (light-on x3 y0) (light-on x3 y1)
    (light-on x3 y3) (light-on x4 y0) (light-on x4 y4)

    (light-off x0 y0) (light-off x0 y1) (light-off x1 y0) (light-off x1 y1) (light-off x1 y2)
    (light-off x2 y1) (light-off x2 y2) (light-off x3 y2) (light-off x3 y4) (light-off x4 y1)
    (light-off x4 y2) (light-off x4 y3)

    (broken x1 y2) (broken x2 y1) (broken x2 y4) (broken x3 y2) (broken x4 y0)

    ; Adicionar luzes aleatórias
    (light-on x5 y5) (light-on x6 y6) (light-on x7 y7) (light-on x8 y8) (light-on x9 y9)
    (light-off x5 y0) (light-off x6 y1) (light-off x7 y2) (light-off x8 y3) (light-off x9 y4)

    ; Adicionar algumas coordenadas "broken" adicionais
    (broken x5 y0) (broken x6 y1) (broken x7 y2) (broken x8 y3) (broken x9 y4)
  )
  (:goal
    ; Definir o objetivo com todas as luzes desligadas
    (and
      (light-off x0 y0) (light-off x0 y1) (light-off x0 y2) (light-off x0 y3) (light-off x0 y4)
      (light-off x1 y0) (light-off x1 y1) (light-off x1 y2) (light-off x1 y3) (light-off x1 y4)
      (light-off x2 y0) (light-off x2 y1) (light-off x2 y2) (light-off x2 y3) (light-off x2 y4)
      (light-off x3 y0) (light-off x3 y1) (light-off x3 y2) (light-off x3 y3) (light-off x3 y4)
      (light-off x4 y0) (light-off x4 y1) (light-off x4 y2) (light-off x4 y3) (light-off x4 y4)
      (not (light-on x0 y0)) (not (light-on x0 y1)) (not (light-on x0 y2)) (not (light-on x0 y3)) (not (light-on x0 y4))
      (not (light-on x1 y0)) (not (light-on x1 y1)) (not (light-on x1 y2)) (not (light-on x1 y3)) (not (light-on x1 y4))
      (not (light-on x2 y0)) (not (light-on x2 y1)) (not (light-on x2 y2)) (not (light-on x2 y3)) (not (light-on x2 y4))
      (not (light-on x3 y0)) (not (light-on x3 y1)) (not (light-on x3 y2)) (not (light-on x3 y3)) (not (light-on x3 y4))
      (not (light-on x4 y0)) (not (light-on x4 y1)) (not (light-on x4 y2)) (not (light-on x4 y3)) (not (light-on x4 y4))
    )
  )
)
