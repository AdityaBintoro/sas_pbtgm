class Activity:
    def __init__(self, day, description, completed=False):
        self.day = day
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = " (Selesai)" if self.completed else ""
        return f"{self.day}: {self.description}{status}"


class Calender:
    def __init__(self):
        self.weekly_schedule = {}

    def add_activity(self, week, day, description):
        if week in self.weekly_schedule:
            print(f"Minggu {week} sudah memiliki aktivitas.")
        else:
            self.weekly_schedule[week] = Activity(day, description)
            print(f"Berhasil menambahkan aktivitas untuk Minggu {week}.")

    def update_activity(self, week, new_day, new_description):
        if week in self.weekly_schedule:
            self.weekly_schedule[week].day = new_day
            self.weekly_schedule[week].description = new_description
            print(f"Berhasil mengubah aktivitas untuk Minggu {week}.")
        else:
            print(f"Minggu {week} tidak ditemukan.")

    def mark_completed(self, week):
        if week in self.weekly_schedule:
            self.weekly_schedule[week].mark_completed()
            print(f"Tugas untuk Minggu {week} ditandai selesai.")
        else:
            print(f"Minggu {week} tidak ditemukan.")

    def display_schedule(self):
        if not self.weekly_schedule:
            print("Belum ada jadwal aktivitas.")
            return

        print("Jadwal Aktivitas Mingguan:")
        for week, activity in sorted(self.weekly_schedule.items()):
            print(f"Minggu {week}: {activity}")


def main():
    calendar = Calender()

    while True:
        print("\n=== Kalender Aktivitas Mingguan ===")
        print("1. Tambah Aktivitas")
        print("2. Tampilkan Jadwal")
        print("3. Ubah Aktivitas")
        print("4. Tandai Tugas Selesai")
        print("5. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            week = input("Masukkan minggu (contoh: 1): ")
            day = input("Masukkan hari (contoh: Senin): ")
            description = input("Masukkan deskripsi aktivitas: ")
            calendar.add_activity(week, day, description)
        elif choice == "2":
            calendar.display_schedule()
        elif choice == "3":
            week = input("Masukkan minggu yang ingin diubah (contoh: 1): ")
            new_day = input("Masukkan hari baru: ")
            new_description = input("Masukkan deskripsi baru: ")
            calendar.update_activity(week, new_day, new_description)
        elif choice == "4":
            week = input("Masukkan minggu yang ingin ditandai selesai (contoh: 1): ")
            calendar.mark_completed(week)
        elif choice == "5":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
