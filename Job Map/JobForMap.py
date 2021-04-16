class Job:
    jobName = "DNE"
    nextJobs = [] # Array of Jobs

    def __init__(self, jobName, nextJobs = []):
        self.jobName = jobName
        self.nextJobs = nextJobs

    def addNextJob(self, nextJob):
        self.nextJobs.append(nextJob)

    # Upgrade Job
    def upgradeJob(self):
        for i in range(0,len(self.nextJobs)):
            print("{} for {}".format(i, self.nextJobs[i].jobName))
        self = self.nextJobs[int(input("Choose: "))]
        print("You have chosen to be: {}".format(self.jobName))

    # Show Entire Tree [ADMIN]
    def showJobTree(self, max):
        print(self.jobName)
        self.showJobTreeHelper(1, max)

    def showJobTreeHelper(self, num, max):
        for i in range(0,len(self.nextJobs)):
            for _j in range(0,num):
                print("-", end = " ")
            print("{}".format(self.nextJobs[i].jobName))
            if (len(self.nextJobs[i].nextJobs) > 0 and num < max):
                self.nextJobs[i].showJobTreeHelper(num + 1, max)

    # Go Down Tree [ADMIN]
    def upgradeSimulation(self):
        while (len(self.nextJobs) > 0):
            for i in range(0,len(self.nextJobs)):
                print("{} for {}".format(i, self.nextJobs[i].jobName))
            self = self.nextJobs[int(input("Choose: "))]
            print("You have chosen to be: {}".format(self.jobName))
