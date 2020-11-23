from experiments import utility


def run_experiment():
	"""
	Experiment II: Noam Chomsky --> https://en.wikipedia.org/wiki/Noam_Chomsky
	"""
	noam_context='Avram Noam Chomsky (born December 7, 1928) is an American linguist, philosopher, cognitive \
	        scientist, historian, social critic, and political activist. Sometimes called "the father of \
	        modern linguistics", Chomsky is also a major figure in analytic philosophy and one of the \
	        founders of the field of cognitive science. He holds a joint appointment as Institute \
	        Professor Emeritus at the Massachusetts Institute of Technology (MIT) and Laureate Professor \
	        at the University of Arizona, and is the author of more than 100 books on topics such as \
	        linguistics, war, politics, and mass media. Ideologically, he aligns with anarcho-syndicalism \
	        and libertarian socialism.'

	question_1="When was Chomsky born?"
	print("question #1: {} --> answer: {}".format(question_1, utility.get_answer(question_1, noam_context)))

	question_2="What month was Chomsky born?"
	print("question #2: {} --> answer: {}".format(question_2, utility.get_answer(question_2, noam_context)))

	question_3="Who is Noam Chomsky?"
	print("question #2: {} --> answer: {}".format(question_3, utility.get_answer(question_3, noam_context)))

	question_4="What universities is Chomsky a professor at?"
	print("question #3: {} --> answer: {}".format(question_4, utility.get_answer(question_4, noam_context)))

	question_5="How many books Chomsky has been author of?"
	print("question #4: {} --> answer: {}".format(question_5, utility.get_answer(question_5, noam_context)))

	question_6="What topics has Chomsky written books in?"
	print("question #5: {} --> answer: {}".format(question_6, utility.get_answer(question_6, noam_context)))

	question_7="What is Chomsky first name?"
	print("question #7: {} --> answer: {}".format(question_7, utility.get_answer(question_7, noam_context)))

	question_8="What is Noam Chomsky nationality?"
	print("question #8: {} --> answer: {}".format(question_8, utility.get_answer(question_8, noam_context)))
