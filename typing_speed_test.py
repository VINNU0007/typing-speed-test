import time 
print("\n----TYPING SPEED TEST----")

input("press enter to start......")
start = time.time()
text = input("\n type anything: ")
end = time.time()
time_taken = end - start
words = len(text.split())
wpm = (words / time_taken) * 60
accuracy = 100
print("\n RESULT")

print(f"⏰ Time: {time_taken:.2f}s")
print(f"⚡ Speed: {wpm:.0f} wpm")
print(f"🎯 Accuracy: {accuracy:.0f}%")