
def get_event_date(event):
	return event.date

def current_users(events):
	events.sort(key=get_event_date)
	machines = {}
	for event in events:
		if event.machine not in machines:
			machines[event.machine] = set()
		if event.etype == "login":
			machines[event.machine].add(event.user)
		elif event.etype == "logout":
			machines[event.machine].remove(event.user)
	return machines

def generate_report(machines):
	for machine, users in machines.items():
		if len(users) > 0:
			user_list = ", ".join(users)
			print("{}: {}".format(machine, user_list))

class Event:
	def __init__(self, date, etype, machine, user):
		self.date = date
		self.etype = etype
		self.machine = machine
		self.user = user

events = [
	Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
	#Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
	Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
	#Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
	Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
	Event("2020-01-23 11:24:35", "login", "mailserver.local", "chris"),
]

users = current_users(events)
print(users)

generate_report(users)
