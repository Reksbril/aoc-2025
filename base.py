class Solution:
    def __init__(self, full_input, short_input, short_result):
        self.full_input = f"data/{full_input}"
        self.short_input = f"data/{short_input}"
        self.short_result = short_result

    def parse(self, file_data):
        pass

    def run(self, solution):
        with open(self.short_input) as f:
            parsed_data = self.parse(f.readlines())

        solution_result = solution(parsed_data)
        if solution_result != self.short_result:
            print(f"{solution_result} != {self.short_result}")
            return

        print("Short result passed!")

        with open(self.full_input) as f:
            parsed_data = self.parse(f.readlines())

        print(solution(parsed_data))
