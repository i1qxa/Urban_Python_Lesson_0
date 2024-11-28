from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname: str = nickname
        self.password: int = hash(password)
        self.age: int = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title: str = title
        self.duration: int = duration
        self.time_now: int = time_now
        self.adult_mode: bool = adult_mode


class UrTube:
    def __init__(self, users: list[User] = [], videos: list[Video] = [], current_user: User = None):
        self.users: list[User] = users
        self.videos: list[Video] = videos
        self.current_user: User = current_user

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    self.current_user = user
                    break

    def register(self, nickname: str, password: str, age: int):
        if any(nickname == user.nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if not any(video.title == exist_video.title for exist_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word: str) -> list[str]:
        list_titles = []
        for video in self.videos:
            if video.title.lower().__contains__(search_word.lower()):
                list_titles.append(video.title)
        return list_titles

    def watch_video(self, video_title: str):
        for video in self.videos:
            if video.title == video_title:
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                elif video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(0, video.duration):
                        sleep(1)
                        video.time_now = i + 1
                        print(video.time_now)
                    print("Конец видео")
                break


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')
