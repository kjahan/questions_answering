from experiments import utility


def run_experiment():
      """
      Experiment I: ELIZA --> https://en.wikipedia.org/wiki/ELIZA
      """
      eliza_context='ELIZA is an early natural language processing computer program created from 1964 to 1966 at \
                  the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum. Created to demonstrate \
                  the superficiality of communication between humans and machines, Eliza simulated \
                  conversation by using a "pattern matching" and substitution methodology that gave users an \
                  illusion of understanding on the part of the program, but had no built in framework for \
                  contextualizing events. Directives on how to interact were provided by "scripts", \
                  written originally in MAD-Slip, which allowed ELIZA to process user inputs and engage \
                  in discourse following the rules and directions of the script. The most famous script, \
                  DOCTOR, simulated a Rogerian psychotherapist (in particular, Carl Rogers, who was \
                  well-known for simply parroting back at patients what they would just said), and used \
                  rules, dictated in the script, to respond with non-directional questions to user inputs. \
                  As such, ELIZA was one of the first chatterbots and one of the first programs capable of \
                  attempting the Turing test.'

      question_1='What programming language was ELIZA written in?'
      print("question #1: {} --> answer: {}".format(question_1, utility.get_answer(question_1, eliza_context)))

      question_2='Who invented ELIZA?'
      print("question #2: {} --> answer: {}".format(question_2, utility.get_answer(question_2, eliza_context)))

      question_3='What is ELIZA?'
      print("question #3: {} --> answer: {}".format(question_3, utility.get_answer(question_3, eliza_context)))

      question_4='Is ELIZA a human?'
      print("question #4: {} --> answer: {}".format(question_4, utility.get_answer(question_4, eliza_context)))

      question_5='Where was ELIZA created at?'
      print("question #5: {} --> answer: {}".format(question_5, utility.get_answer(question_5, eliza_context)))

      question_6='Did ELIZA pass Turing test?'
      print("question #6: {} --> answer: {}".format(question_6, utility.get_answer(question_6, eliza_context)))
