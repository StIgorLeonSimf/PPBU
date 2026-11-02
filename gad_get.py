from abc import ABC, abstractmethod


class Gadget(ABC):
    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def inet(self):
        pass

    @abstractmethod
    def video(self):
        pass

    # class Smartphone(Gadget):
    #     def talk(self):
    #         print("talk")
    #
    #     def inet(self):
    #         print("inet")
    #
    #     def video(self):
    #         print("video")

    # class Telephone(Gadget):
    #     def talk(self):
    #         print("talk")

    def inet(self):
        pass

    def video(self):
        pass


class Talk(ABC):
    @abstractmethod
    def talk(self):
        pass


class Video(ABC):
    @abstractmethod
    def video(self):
        pass


class Inet(ABC):
    @abstractmethod
    def inet(self):
        pass


classes = (Talk, Inet, Video)


class Smartphone(*classes):

    def talk(self):
        print("talk")

    def inet(self):
        print("inet")

    def video(self):
        print("video")


class Telephone(Talk):
    def talk(self):
        print("talk")


sm = Smartphone()
sm.talk()
sm.inet()
sm.video()