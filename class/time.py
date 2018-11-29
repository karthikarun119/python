class TimeClass:
        def __init__(self,x,y,z):
                self.hour = x
                self.minute = y
                self.second = z

        def __str__(self):
            return "({:02d}:{:02d}:{:02d})".format(self.hour, self.minute, self.second)

        def time_to_int(self,time):

            minutes = (time.hour * 60) + time.minute
            seconds = (minutes * 60) + time.second
            return seconds

        def int_to_time(self,seconds):
                time = TimeClass(0,0,0)
                minutes,time.second=divmod(seconds,60)
                time.hour,time.minute=divmod(minutes,60)
                return time

        def add_time(self,t1,t2):
                seconds = self.time_to_int(t1) + self.time_to_int(t2)
                # Call method int_to_time() using self keyword.
                return self.int_to_time(seconds)


# First time object create that time set value is 0 of hour,minute and second
t1 = TimeClass(0,0,0)
start=TimeClass(9,45,00)
running=TimeClass(1,35,00)
print(t1.add_time(start,running))