(define (domain lightsout)
  (:requirements :adl :strips)
  (:types
    cell - object
  )
  (:predicates
    (light-on ?x ?y - cell) ; A luz está ligada na posição ?x ?y
    (light-off ?x ?y - cell) ; A luz está desligada na posição ?lon
    (inc ?a ?b - cell)                  ; indica um incremento entre celulas
    (dec ?a ?b - cell)                  ; indica um decremento entre celulas
    (broken ?x ?y - cell) ; a celula não esta quebrada
)

  (:action switch-on-off
      :parameters (?x ?y - cell)
      :precondition (or (light-on ?x ?y) (light-off ?x ?y))
      :effect (and 
        (when (and (light-on ?x ?y) (not (broken ?x ?y))) (and (light-off ?x ?y) (not (light-on ?x ?y))))
        (when (and (light-off ?x ?y) (not (broken ?x ?y))) (and (light-on ?x ?y) (not (light-off ?x ?y))))
        (forall (?w - cell)
          (when 
            (or
              (inc ?x ?w)
              (inc ?w ?y)
              (dec ?x ?w)
              (dec ?w ?y)
            )
            (and
              (when 
                (light-on ?x ?w)
                (and 
                (light-off ?x ?w)
                (not (light-on ?x ?w))
                )
              )
              (when 
                (light-off ?x ?w)
                (and 
                (light-on ?x ?w)
                (not (light-off ?x ?w))
                )
              )
              (when 
                (light-on ?w ?y)
                (and 
                (light-off ?w ?y)
                (not (light-on ?w ?y))
                )
              )
              (when 
                (light-off ?w ?y)
                (and 
                (light-on ?w ?y)
                (not (light-off ?w ?y))
                )
              )
            )
          )
        )
      )
  )
)