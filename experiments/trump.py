from experiments import utility


def run_experiment():
	"""
	Experiment III: Donald Trump --> https://en.wikipedia.org/wiki/Donald_Trump
	"""
	trump_context="Trump was born and raised in Queens, a borough of New York City, and received a \
	            bachelor's degree in economics from the Wharton School. He took charge of his family's \
	            real-estate business in 1971, renamed it The Trump Organization, and expanded its \
	            operations from Queens and Brooklyn into Manhattan. Trump later started various side \
	            ventures, mostly by licensing his name. He bought the Miss Universe brand of beauty \
	            pageants in 1996, and sold it in 2015. Trump and his businesses have been involved in \
	            more than 4,000 state and federal legal actions, including six bankruptcies. He produced \
	            and hosted The Apprentice, a reality television series, from 2003 to 2015. As of 2020, \
	            Forbes estimated his net worth to be $2.1 billion."

	question_1="When was Trump born?"
	print("question #1: {} --> answer: {}".format(question_1, utility.get_answer(question_1, trump_context)))

	question_2="Where was Trump born?"
	print("question #2: {} --> answer: {}".format(question_2, utility.get_answer(question_2, trump_context)))

	question_3="What is Trump business?"
	print("question #3: {} --> answer: {}".format(question_3, utility.get_answer(question_3, trump_context)))

	question_4="How much is Trump wealth?"
	print("question #4: {} --> answer: {}".format(question_4, utility.get_answer(question_4, trump_context)))

	question_5="What is Trump nationality?"
	print("question #5: {} --> answer: {}".format(question_5, utility.get_answer(question_5, trump_context)))

	question_6="How many times Trump businesses have declared bankruptcies?"
	print("question #6: {} --> answer: {}".format(question_6, utility.get_answer(question_6, trump_context)))

	question_7="What school did Trump go to?"
	print("question #7: {} --> answer: {}".format(question_7, utility.get_answer(question_7, trump_context)))
