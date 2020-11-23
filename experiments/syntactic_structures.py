from experiments import utility


def run_experiment():
	"""
	Experiment IV: Syntactic Structures --> https://en.wikipedia.org/wiki/Syntactic_Structures#Impact_on_other_disciplines
	"""
	syntactic_context="Syntactic Structures is an influential work in linguistics by American linguist Noam Chomsky, \
					originally published in 1957. It is an elaboration of his teacher's, Zellig Harris's, model \
					of transformational generative grammar. A short monograph of about a hundred pages, Chomsky's \
					presentation is recognized as one of the most significant studies of the 20th century, and \
					in 2011 was selected by Time magazine as one of the 100 most important nonfiction books ever \
					written. It contains the now-famous sentence \"Colorless green ideas sleep furiously\", which \
					Chomsky offered as an example of a grammatically correct sentence that has no discernible \
					meaning. Thus, Chomsky argued for the independence of syntax (the study of sentence structures) \
					from semantics (the study of meaning). The significance of Syntactic Structures lies in Chomsky's \
					persuasion for a biological perspective on language at a time when it was unusual and in the context \
					of formal linguistics where it was unexpected. Chomsky eventually became recognised as one of the \
					founders of what is now known as sociobiology. Another reason for the fame of Syntactic Structures \
					was that Hjelmslev died in 1965 after which generative grammarians were not clear about the origin \
					of the theory. Written when he was still an unknown scholar, Syntactic Structures had a major impact \
					on the study of knowledge, mind and mental processes, being an influential work in the formation of \
					the field of cognitive science. It also significantly influenced research on computers and the \
					brain. Some specialists have questioned the theory, believing it is wrong to describe language as \
					an ideal system. They also say it gives less value to the gathering and testing of data. \
					Nevertheless, American linguistics changed course in the second half of the 20th century as a result of Syntactic Structures."

	question_1="What is Syntactic Structures?"
	print("question #1: {} --> answer: {}".format(question_1, utility.get_answer(question_1, syntactic_context)))

	question_2="Who was the inventor of Syntactic Structures?"
	print("question #2: {} --> answer: {}".format(question_2, utility.get_answer(question_2, syntactic_context)))

	question_3="Why is Syntactic Structures significant?"
	print("question #2: {} --> answer: {}".format(question_3, utility.get_answer(question_3, syntactic_context)))
