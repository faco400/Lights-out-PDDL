(define (problem p01) (:domain lightsout)
(:objects
    x0 x1 x2 y0 y1 y2 - cell
)
  (:init
      (inc x0 x1) (inc x1 x2)
      (inc y0 y1) (inc y1 y2)
      (dec x2 x1) (dec x1 x0)
      (dec y2 y1) (dec y1 y0)

      (light-on x0 y1)
      (light-on x1 y1)
      (light-on x1 y0)
      (light-on x1 y2)
      (light-on x2 y1)

      (light-off x0 y0)
      (light-off x0 y2)
      (light-off x2 y0)
      (light-off x2 y2)

)
  (:goal
    (and (light-off x0 y0) (light-off x0 y1) (light-off x0 y2)
    (light-off x1 y0) (light-off x1 y1) (light-off x1 y2)
    (light-off x2 y0) (light-off x2 y1) (light-off x2 y2)
    (not (light-on x0 y0)) (not (light-on x0 y1)) (not (light-on x0 y2))
    (not (light-on x1 y0)) (not (light-on x1 y1)) (not (light-on x1 y2))
    (not (light-on x2 y0)) (not (light-on x2 y1)) (not (light-on x2 y2))
    )
  )
)
