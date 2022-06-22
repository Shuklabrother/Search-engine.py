import wikipedia
import pyfiglet

word = pyfiglet.figlet_format("KAREN")
print(word)

while True:
      engine=input ("Search: ")

      def my_summary():
               summ=wikipedia.summary(engine)
               return summ
      val = my_summary()
      print(val)
 
