# -------------------------------------------------------1--------------------------------------------------------------
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности (duration)
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
print("Enter duration or 'q' to exit the program.")
duration = ''
while duration != 'q':
    duration = (input("Enter time in seconds: "))
    if duration == 'q':
        break
    else:
        try:
            duration = int(duration)
        except ValueError:
            print("You can't use letters!")
        else:
            hours = duration // 3600
            remainder_secs = duration % 3600
            minutes = remainder_secs // 60
            remainder_secs = remainder_secs % 60
            secs = remainder_secs

            days = 0
            while hours >= 24:
                days += 1
                hours = hours - 24
            # Ветвление для вывода.
            if not days:
                if hours:
                    print(f" {hours:02} h - {minutes:02} m - {secs:02} s")
                else:
                    if minutes:
                        print(f"{minutes:02} m - {secs:02} s")
                    else:
                        if secs:
                            print(f"{secs:02} s")
            else:
                print(f"{days:02} d - {hours:02} h - {minutes:02} m - {secs:02} s")
