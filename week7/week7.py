# def observed():
#     observations = {"car", "sky scrapper", "sky scrapper", "house", "bike", "house", "car"}
#     return observations
# def run_task1():
#     result = observed()
#     print(result)
# if __name__=="__main__":
#     run_task1()
def observed_items():
    observations = []
    for _ in range(7):
        observation = input("Please enter the Observations.")
        observations.append(observation)
    return observations
def run_task2():
    print("Counting observations.")
    observations = observed_items()
    observation_set = set()
    for item in observations:
        print(f"{item} observed {count} times.")
if __name__=="__main__":
    run_task2()

