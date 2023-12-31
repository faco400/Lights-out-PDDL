import sys
import subprocess
import os

regex = r"\(switch-on-off\s+(\w+)\s+(\w+)\)"
DOMAIN = 'lightsout.pddl'
PLANNER = '/tmp/dir/software/planners/madagascar/M' # bom no AGILE
# PLANNER = '/tmp/dir/software/planners/downward/fast-downward.py' 
# PLANNER = '/tmp/dir/software/planners/downward-fdss23/fast-downward.py' 
# PLANNER = '/tmp/dir/software/planners/scorpion-maidu/fast-downward.py' 
PROBLEM = 'problem.pddl'
OUTPUT = 'sas_plan'

# gera goal do problema
def generateGoal(qtde):
  on_goal = ''
  off_goal = ''
  for i in range(qtde):
    for j in range(qtde):
      off_goal += f'(light-off x{i} y{j})\n'
      on_goal += f'(not (light-on x{i} y{j}))\n'
  
  return on_goal, off_goal

# gera predicados light-on e light-off e broken
def generateLightOnOffBroken(i_parameters):
  on_predicate = ''
  off_predicate = ''
  broken_predicate = ''

  count_lines = 0
  for line in i_parameters:
    count_column = 0
    for character in line[:-1]:
      if character == 'D' or character == 'd':
        off_predicate += f'(light-off x{count_lines} y{count_column})\n'
        if character == 'd':
          broken_predicate += f'(broken x{count_lines} y{count_column})\n'

      if character == 'L' or character == 'l':
        on_predicate += f'(light-on x{count_lines} y{count_column})\n'
        if character == 'l':
          broken_predicate += f'(broken x{count_lines} y{count_column})\n'
      
      count_column += 1
    count_lines += 1

  return on_predicate, off_predicate, broken_predicate


# gera incrementos para o init do problema
def generateIncs(qtde):
  predicate_x = ''
  predicate_y = ''
  for i in range(qtde-1):
    predicate_x += f'(inc x{i} x{i+1}) '
    predicate_y += f'(inc y{i} y{i+1}) '
  return predicate_x, predicate_y
  
# gera decrementos para o init do problema
def generateDecs(qtde):
  predicate_x = ''
  predicate_y = ''
  for i in range(qtde-1, 0, -1):
    predicate_x += f'(dec x{i} x{i-1}) '
    predicate_y += f'(dec y{i} y{i-1}) '
  return predicate_x, predicate_y
# gera objetos do arquivo de problema
def generateObjects(qtde):
  objects = ''
  for i in range(qtde):
    objects += f'x{i} y{i} '
  
  return objects

# Gera arquivo de domínio
def generateDomain():
  if not DOMAIN:
    print('No path specified for domain')
  else:
    with open (DOMAIN, 'w+') as domain:
      domain.write(
        """
        (define (domain lightsout)
  (:requirements :adl)
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
        """)
  pass

# Gera arquivo de problema
def generateProblem(i_parameters):
  if not PROBLEM:
    print('No path specified for problem')
    return
  
  objects_count = len(i_parameters)
  objects = generateObjects(objects_count)
  incsX, incsY = generateIncs(objects_count)
  decsX, decsY = generateDecs(objects_count)
  on, off, broken = generateLightOnOffBroken(i_parameters)
  goal_on, goal_off = generateGoal(objects_count)



  with open(PROBLEM, 'w+') as problem:
    problem.write(
  f"""
  (define (problem p01) (:domain lightsout)
  (:objects
  {objects} - cell
  )
  (:init
  {incsX}
  {incsY}
  {decsX}
  {decsY}

  {on}

  {off}

  {broken}
  )

  (:goal
  (and
  {goal_off}
  {goal_on}
  )
  )
  )
  """)
  pass

# Leitura da entrada
def readInput():
  input_parameters = []
  for line in sys.stdin:
    input_parameters.append(line)
   
  # print(input_parameters)
  return input_parameters

# Chama o planejador e executa com domínio e problema gerados
def callPlanner():
  # subprocess.call([PLANNER, '--alias', 'lama-first', DOMAIN, PROBLEM], stdout=subprocess.DEVNULL) # para fastdownard
  # subprocess.call([PLANNER, '--search-time-limit', '800' , '--plan-file', OUTPUT, '--alias', 'seq-sat-maidu', DOMAIN, PROBLEM], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # para fastdownard  com lama 2011 ou stone soup
  # subprocess.call([PLANNER, '--plan-file', OUTPUT, '--search-time-limit', '800','--alias', 'seq-opt-fdss-2023', DOMAIN, PROBLEM], stdout=subprocess.DEVNULL) # Bom para optimal
  subprocess.call([PLANNER, DOMAIN, PROBLEM, '-o', OUTPUT, '-Q', '-B', '0.3','-P', '0'], stdout=subprocess.DEVNULL) # Não foi feito testes ainda, poderia superar o de baixo??
  # subprocess.call([PLANNER, DOMAIN, PROBLEM, '-o', OUTPUT, '-Q'], stdout=subprocess.DEVNULL) # para madagascar -> Bom no AGILE e Melhor no SAT até o momento

# read plan output
def readPlan():
  coordinates = ''
  x = ''
  y = ''

  # read fastdownward plan com lama first e seq-opt-fdss-2
  # with open(OUTPUT,'r') as output:
  #   for line in output:
  #     if 'cost' in line:
  #       pass
  #     else:
  #       plan = line[15:-2]
  #       xy = plan.split(' ')
  #       x = xy[0].strip('x')
  #       y = xy[1].strip('y')
  #       coordinates += f'({x}, {y});'
  # print(coordinates[:-1]+'\n')

  # read fastdownward plan com seq-sat-lama-2011 ou stone soup (fdss-2)
  # for i in range(1,100,1):
  #   if os.path.exists(f'{OUTPUT}.{i}'):
  #     plan_file = f'{OUTPUT}.{i}'
  #   else:
  #     plan_file = f'{OUTPUT}.{i-1}'
  #     break
  # with open(plan_file,'r') as output:
  #   for line in output:
  #     if 'cost' in line:
  #       pass
  #     else:
  #       plan = line[15:-2]
  #       xy = plan.split(' ')
  #       x = xy[0].strip('x')
  #       y = xy[1].strip('y')
  #       coordinates += f'({x}, {y});'
  # print(coordinates[:-1]+'\n')

  # read madagascar plan
  with open(OUTPUT,'r') as output:
    for line in output:
      if 'cost' in line:
        pass
      else:
        startX = line.rfind('x')
        plan = line[startX:-2]
        xy = plan.split(' ')
        x = xy[0].strip('x')
        y = xy[1].strip('y')
        coordinates += f'({x}, {y});'
  print(coordinates[:-1]+'\n')

if __name__ == "__main__":
  i_parameters = readInput()
  generateDomain()
  generateProblem(i_parameters)
  callPlanner()
  readPlan()
