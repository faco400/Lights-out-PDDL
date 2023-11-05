(define (domain lights-out)
  (:requirements :adl :typing)
  (:types
    cell - object
  )
  (:predicates
    (position ?p -  cell) ; posição de inicio
    (light-on ?lon - cell)    ; A luz está ligada na posição ?x
    (light-off ?loff - cell)   ; A luz está desligada na posição ?x
    (button-broken ?c - cell)  ; O botão na posição ?x está quebrado
    (connected ?c1 - cell ?c2 - cell) ; conecta as celulas da grid
  )

  (:action switch-off
      :parameters (?c - cell)
      :precondition (and (light-on ?c) )
      :effect (and (light-off ?c) (not (light-on ?c) ) )
  )

  (:action move
    :parameters (?from - cell ?to - cell)
    :precondition
    (and
        (position ?from)
    )
    :effect
    (and
        (position ?to)
        (not (position ?from))
    )
)
  

  ; (:action switch-on
  ;   :parameters (?x - light)
  ;   :precondition (and (light-off ?x) (not (button-broken ?x)))
  ;   :effect (and (light-on ?x) (not (light-off ?x)))
  ; )

  ; (:action switch-off
  ;   :parameters (?x - light)
  ;   :precondition (and (light-on ?x) (not (button-broken ?x)))
  ;   :effect (and (light-off ?x) (not (light-on ?x)))
  ; )

  ; (:action press-button
  ;   :parameters (?x - light)
  ;   :precondition (and (not (button-broken ?x)) (light-on ?x))
  ;   :effect (and (not (light-on ?x)))
  ; )
)