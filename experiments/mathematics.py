from experiments import utility


def run_triangle_experiment():
	"""
	Experiment V: Triangle --> https://en.wikipedia.org/wiki/Triangle
	"""
	triangle_context="A triangle is a polygon with three edges and three vertices. It is one of the basic shapes in geometry. \
						A triangle with vertices A, B, and C is denoted triangle ABC. In Euclidean \
						geometry, any three points, when non-collinear, determine a unique triangle and simultaneously, a unique plane \
						(i.e. a two-dimensional Euclidean space). In other words, there is only one plane that contains that triangle, \
						and every triangle is contained in some plane. If the entire geometry is only the Euclidean plane, there is only \
						one plane and all triangles are contained in it; however, in higher-dimensional Euclidean spaces, this is no \
						longer true. This article is about triangles in Euclidean geometry, and in particular, the Euclidean plane, \
						except where otherwise noted."

	question_1="How many edges a triangle has?"
	print("question #1: {} --> answer: {}".format(question_1, utility.get_answer(question_1, triangle_context)))

	question_2="How many vertices a triangle has?"
	print("question #2: {} --> answer: {}".format(question_2, utility.get_answer(question_2, triangle_context)))

	question_3="What is triangle?"
	print("question #3: {} --> answer: {}".format(question_3, utility.get_answer(question_3, triangle_context)))