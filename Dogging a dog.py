import pygame
import sys
import requests
from io import BytesIO
import tempfile
import cv2
import random
import time

# ---------- INIT ----------
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dog vs Mushroomer")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
fight_font = pygame.font.SysFont(None, 48)

# ---------- LOAD IMAGES FROM GITHUB ----------
def load_image(url, size):
    try:
        if "github.com" in url and "/blob/" in url:
            url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
        data = requests.get(url).content
        img = pygame.image.load(BytesIO(data)).convert_alpha()
        return pygame.transform.scale(img, size)
    except Exception as e:
        print(f"Помилка завантаження зображення: {e}")
        img = pygame.Surface(size)
        img.fill((100, 150, 50))
        return img

# Звичайні зображення для початкової частини
DOG_NORMAL_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/Собака-removebg-preview.png"
MUSHROOM_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/Гриб.png"
MUSHROOMER_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/Goomba-removebg-preview.png"

# ОСОБЛИВЕ зображення для собаки в бою
DOG_FIGHT_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA_%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2026-01-15_134510-removebg-preview%20(1).png"

# Зображення поліцейського та фонів
POLICE_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/1675858971_grizly-club-p-politseiskii-klipart-dlya-detei-31-removebg-preview.png"
BACKGROUND_1_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-23%20130527.png"
BACKGROUND_2_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-23%20132701.png"
BACKGROUND_3_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-05-23%20133246.png"

MUSIC_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/NXGHT_DJ_ANXVAR_DJ_ZAP_-_BLUE_HORIZON_FUNK_-_SLOWED_(mp3.pm).mp3"
BATTLE_MUSIC_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0418%20(online-audio-converter.com).mp3"
BATTLEFIELD_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/trava_pole_derevo_135338_3840x2160.jpg"

CUTSCENE_1_VIDEO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/cutscene.MP4"
CUTSCENE_1_AUDIO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/cutscene.mp3"

CUTSCENE_2_VIDEO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/Cutscene%202.mp4"
CUTSCENE_2_AUDIO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/Cutscene-2.mp3"

# КАТСЦЕНИ ДЛЯ РЕЗУЛЬТАТУ БОЮ
WIN_CUTSCENE_VIDEO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0418%20(1)(1).mp4"
WIN_CUTSCENE_AUDIO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0418%20(1)(1)%20(online-audio-converter.com).mp3"
LOSE_CUTSCENE_VIDEO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0418%20(1)(2).mp4"
LOSE_CUTSCENE_AUDIO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0418%20(1)(2)%20(online-audio-converter.com).mp3"

# Нові катсцени для поліцейського зі звуком
POLICE_CUTSCENE_1_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0523(1).mp4"
POLICE_CUTSCENE_1_AUDIO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0523(1)%20(online-audio-converter.com).mp3"
POLICE_CUTSCENE_2_URL = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0523%20(3)(1).mp4"
POLICE_CUTSCENE_2_AUDIO = "https://raw.githubusercontent.com/Artemchick2015/Dogging-a-Dog/main/0523%20(3)(1)%20(online-audio-converter.com).mp3"

print("Завантаження зображень...")
dog_normal_img = load_image(DOG_NORMAL_URL, (80, 80))
dog_fight_img = load_image(DOG_FIGHT_URL, (112, 112))
mushroomer_normal_img = load_image(MUSHROOMER_URL, (80, 80))
mushroomer_fight_img = load_image(MUSHROOMER_URL, (112, 112))
mushroom_img = load_image(MUSHROOM_URL, (40, 40))
battlefield_img = load_image(BATTLEFIELD_URL, (WIDTH, HEIGHT))

# ЗБІЛЬШЕНИЙ ПОЛІЦЕЙСЬКИЙ - в 10 разів більше (600x800)
POLICE_WIDTH = 600
POLICE_HEIGHT = 800
police_img = load_image(POLICE_URL, (POLICE_WIDTH, POLICE_HEIGHT))

background_1_img = load_image(BACKGROUND_1_URL, (WIDTH, HEIGHT))
background_2_img = load_image(BACKGROUND_2_URL, (WIDTH, HEIGHT))
background_3_img = load_image(BACKGROUND_3_URL, (WIDTH, HEIGHT))
print("Зображення завантажено!")

# ---------- LOAD MUSIC ----------
def load_music(url):
    try:
        if "github.com" in url and "/blob/" in url:
            url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
        music_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        music_file.write(requests.get(url).content)
        music_file.close()
        return music_file.name
    except Exception as e:
        print(f"Помилка завантаження музики: {e}")
        return None

# Завантажуємо музику
chase_music_file = load_music(MUSIC_URL)
battle_music_file = load_music(BATTLE_MUSIC_URL)

# ---------- CUTSCENE ----------
def play_cutscene(video_url, audio_url=None, fps=33):
    try:
        if "github.com" in video_url and "/blob/" in video_url:
            video_url = video_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
        
        video_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        video_temp.write(requests.get(video_url).content)
        video_temp.close()

        cap = cv2.VideoCapture(video_temp.name)
        delay = int(1000 / fps)
        
        if audio_url:
            if "github.com" in audio_url and "/blob/" in audio_url:
                audio_url = audio_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            audio_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            audio_temp.write(requests.get(audio_url).content)
            audio_temp.close()
            pygame.mixer.music.load(audio_temp.name)
            pygame.mixer.music.play()

        while cap.isOpened():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cap.release()
                    pygame.quit()
                    sys.exit()

            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            frame = pygame.transform.scale(frame, (WIDTH, HEIGHT))

            screen.blit(frame, (0, 0))
            pygame.display.update()
            pygame.time.delay(delay)

        cap.release()
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"Помилка відтворення катсцени: {e}")

# ---------- FADE OUT MUSIC ----------
def fade_out_music(duration_ms=2000):
    if not pygame.mixer.music.get_busy():
        return
    
    steps = 20
    step_duration = duration_ms // steps
    
    for step in range(steps, -1, -1):
        volume = step / steps
        pygame.mixer.music.set_volume(volume)
        pygame.time.delay(step_duration)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(1.0)

# ---------- FADE SCREEN ----------
def fade_screen():
    fade_overlay = pygame.Surface((WIDTH, HEIGHT))
    for i in range(0, 255, 5):
        fade_overlay.set_alpha(i)
        fade_overlay.fill((0, 0, 0))
        screen.blit(fade_overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)
    for i in range(255, 0, -5):
        fade_overlay.set_alpha(i)
        fade_overlay.fill((0, 0, 0))
        screen.blit(fade_overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)

# ---------- DRAW HEALTH BARS ----------
def draw_health_bars(dog_health, mushroomer_health, hits_landed):
    dog_bar_width = 150
    dog_bar_height = 15
    dog_health_percent = max(0, dog_health / 100)
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, dog_bar_width, dog_bar_height))
    pygame.draw.rect(screen, (0, 255, 0), (20, 20, dog_bar_width * dog_health_percent, dog_bar_height))
    
    mushroomer_bar_width = 150
    mushroomer_bar_height = 15
    mushroomer_health_percent = max(0, mushroomer_health / 100)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH - 170, 20, mushroomer_bar_width, mushroomer_bar_height))
    pygame.draw.rect(screen, (0, 255, 0), (WIDTH - 170, 20, mushroomer_bar_width * mushroomer_health_percent, mushroomer_bar_height))
    
    hits_text = font.render(f"Удари: {hits_landed}/15", True, (255, 255, 255))
    screen.blit(hits_text, (WIDTH//2 - 60, 20))

# ---------- GAME RESET ----------
def reset_game():
    global dog, mushroomer, mushrooms, game_state, chase_start, dog_health, mushroomer_health, battle_result, hits_landed, last_mushroomer_attack_time
    global police, police_background, police_x, police_y, show_pickup_text
    
    dog = pygame.Rect(WIDTH//2, HEIGHT//2, 112, 112)
    mushroomer = pygame.Rect(50, 50, 112, 112)

    mushrooms = []
    for _ in range(10):
        x = random.randint(50, WIDTH-90)
        y = random.randint(50, HEIGHT-90)
        mushrooms.append(pygame.Rect(x, y, 40, 40))

    game_state = "collect"
    chase_start = 0
    dog_health = 100
    mushroomer_health = 100
    battle_result = None
    hits_landed = 0
    last_mushroomer_attack_time = 0
    
    # Змінено розмір поліцейського для нового Rect
    police = pygame.Rect(WIDTH//2 - POLICE_WIDTH//2, HEIGHT//2 - POLICE_HEIGHT//2, POLICE_WIDTH, POLICE_HEIGHT)
    police_background = 1
    police_x = WIDTH//2 - POLICE_WIDTH//2
    police_y = HEIGHT//2 - POLICE_HEIGHT//2
    show_pickup_text = False
    
    try:
        pygame.mixer.music.stop()
    except:
        pass

# ---------- ПОЧАТКОВІ ЗМІННІ ----------
dog = pygame.Rect(WIDTH//2, HEIGHT//2, 112, 112)
mushroomer = pygame.Rect(50, 50, 112, 112)

mushrooms = []
for _ in range(10):
    x = random.randint(50, WIDTH-90)
    y = random.randint(50, HEIGHT-90)
    mushrooms.append(pygame.Rect(x, y, 40, 40))

game_state = "collect"
chase_start = 0
dog_health = 100
mushroomer_health = 100
battle_result = None
hits_landed = 0
last_mushroomer_attack_time = 0

# Змінні поліцейського - ЗБІЛЬШЕНИЙ РОЗМІР
police = pygame.Rect(WIDTH//2 - POLICE_WIDTH//2, HEIGHT//2 - POLICE_HEIGHT//2, POLICE_WIDTH, POLICE_HEIGHT)
police_background = 1
police_x = WIDTH//2 - POLICE_WIDTH//2
police_y = HEIGHT//2 - POLICE_HEIGHT//2
show_pickup_text = False

# ---------- MAIN LOOP ----------
running = True
while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if game_state == "lose":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
        
        if game_state == "fight":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if abs(dog.x - mushroomer.x) < 120 and abs(dog.y - mushroomer.y) < 120:
                    mushroomer_health -= random.randint(6, 8)
                    hits_landed += 1
        
        if game_state == "police_level":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t and show_pickup_text:
                play_cutscene(POLICE_CUTSCENE_2_URL, POLICE_CUTSCENE_2_AUDIO, 30)
                fade_screen()
                game_state = "black_screen"
                show_pickup_text = False

    keys = pygame.key.get_pressed()
    speed = 5
    
    # ---------- ВСІ ПЕРСОНАЖІ КЕРУЮТЬСЯ КЛАВІШАМИ WASD ----------
    
    # ---------- ЕТАП 1: ЗБІР ГРИБІВ ----------
    if game_state == "collect":
        if keys[pygame.K_a]: 
            dog.x -= speed
        if keys[pygame.K_d]: 
            dog.x += speed
        if keys[pygame.K_w]: 
            dog.y -= speed
        if keys[pygame.K_s]: 
            dog.y += speed
        dog.clamp_ip(screen.get_rect())
        
        for m in mushrooms[:]:
            if dog.colliderect(m):
                mushrooms.remove(m)

        if not mushrooms:
            game_state = "chase"
            chase_start = pygame.time.get_ticks()
            if chase_music_file:
                pygame.mixer.music.load(chase_music_file)
                pygame.mixer.music.play(-1)

    # ---------- ЕТАП 2: ВТЕЧА 20 СЕКУНД ----------
    elif game_state == "chase":
        if keys[pygame.K_a]: 
            dog.x -= speed
        if keys[pygame.K_d]: 
            dog.x += speed
        if keys[pygame.K_w]: 
            dog.y -= speed
        if keys[pygame.K_s]: 
            dog.y += speed
        dog.clamp_ip(screen.get_rect())
        
        mushroom_speed = 2.2
        if mushroomer.x < dog.x: 
            mushroomer.x += mushroom_speed
        if mushroomer.x > dog.x: 
            mushroomer.x -= mushroom_speed
        if mushroomer.y < dog.y: 
            mushroomer.y += mushroom_speed
        if mushroomer.y > dog.y: 
            mushroomer.y -= mushroom_speed

        if mushroomer.colliderect(dog):
            game_state = "lose"
            fade_out_music(1000)

        elapsed_sec = (pygame.time.get_ticks() - chase_start) // 1000
        if elapsed_sec >= 20:
            fade_out_music(1000)
            
            play_cutscene(CUTSCENE_1_VIDEO, CUTSCENE_1_AUDIO, fps=32)
            fade_screen()
            play_cutscene(CUTSCENE_2_VIDEO, CUTSCENE_2_AUDIO, fps=120)
            
            game_state = "fight"
            dog.x = WIDTH//4
            dog.y = HEIGHT//2 + HEIGHT//4 - 20
            mushroomer.x = WIDTH - 150
            mushroomer.y = HEIGHT//2 + HEIGHT//4 - 20
            last_mushroomer_attack_time = pygame.time.get_ticks()
            
            if battle_music_file:
                pygame.mixer.music.load(battle_music_file)
                pygame.mixer.music.play(-1)

    # ---------- ЕТАП 3: БІЙ ----------
    elif game_state == "fight":
        if keys[pygame.K_a]: 
            dog.x -= speed
        if keys[pygame.K_d]: 
            dog.x += speed
        
        dog.x = max(50, min(WIDTH - 160, dog.x))
        
        mushroom_speed = 1.5
        if mushroomer.x < dog.x: 
            mushroomer.x += mushroom_speed
        if mushroomer.x > dog.x: 
            mushroomer.x -= mushroom_speed
        
        mushroomer.x = max(100, min(WIDTH - 140, mushroomer.x))
        
        if current_time - last_mushroomer_attack_time >= 1500:
            if abs(dog.x - mushroomer.x) < 130 and abs(dog.y - mushroomer.y) < 130:
                dog_health -= random.randint(10, 15)
                last_mushroomer_attack_time = current_time
                pygame.time.delay(50)
        
        # ПЕРЕВІРКА РЕЗУЛЬТАТУ БОЮ
        if hits_landed >= 15:
            fade_out_music(1000)
            fade_screen()
            play_cutscene(WIN_CUTSCENE_VIDEO, WIN_CUTSCENE_AUDIO, fps=30)
            fade_screen()
            play_cutscene(POLICE_CUTSCENE_1_URL, POLICE_CUTSCENE_1_AUDIO, 30)
            fade_screen()
            game_state = "police_level"
            police_background = 1
            police_x = WIDTH//2 - POLICE_WIDTH//2
            police_y = HEIGHT//2 - POLICE_HEIGHT//2
            police.x = police_x
            police.y = police_y
            
        elif dog_health <= 0:
            fade_out_music(1000)
            fade_screen()
            play_cutscene(LOSE_CUTSCENE_VIDEO, LOSE_CUTSCENE_AUDIO, fps=30)
            fade_screen()
            game_state = "lose"

    # ---------- ЕТАП 4: ПОЛІЦЕЙСЬКИЙ РІВЕНЬ (РУХ ВПРАВО ДЛЯ ЗМІНИ ЛОКАЦІЇ) ----------
    elif game_state == "police_level":
        # РУХ ПОЛІЦЕЙСЬКОГО ВЛІВО/ВПРАВО/ВВЕРХ/ВНИЗ
        if keys[pygame.K_a]: 
            police_x -= speed
        if keys[pygame.K_d]: 
            police_x += speed
        if keys[pygame.K_w]: 
            police_y -= speed
        if keys[pygame.K_s]: 
            police_y += speed
        
        # Обмеження руху в межах екрану для збільшеного поліцейського
        police_x = max(0, min(WIDTH - POLICE_WIDTH, police_x))
        police_y = max(0, min(HEIGHT - POLICE_HEIGHT, police_y))
        police.x = police_x
        police.y = police_y
        
        # ПЕРЕХІД МІЖ ЛОКАЦІЯМИ КОЛИ ВПИРАЄМОСЬ В ПРАВУ СТІНУ
        if police_x >= WIDTH - POLICE_WIDTH - 5:
            if police_background == 1:
                police_background = 2
                police_x = 5
                police.x = police_x
                pygame.time.delay(100)
            elif police_background == 2:
                police_background = 3
                police_x = 5
                police.x = police_x
                pygame.time.delay(100)
        
        # Показуємо текст підібрати собаку тільки на 3-му фоні
        show_pickup_text = (police_background == 3)
        
        # Малювання фону
        if police_background == 1:
            screen.blit(background_1_img, (0, 0))
        elif police_background == 2:
            screen.blit(background_2_img, (0, 0))
        elif police_background == 3:
            screen.blit(background_3_img, (0, 0))
        
        # Малювання ЗБІЛЬШЕНОГО поліцейського
        screen.blit(police_img, police)
        
        if show_pickup_text:
            pickup_text = font.render("T - підібрати собаку", True, (255, 255, 255))
            text_rect = pickup_text.get_rect(center=(WIDTH//2, HEIGHT - 50))
            screen.blit(pickup_text, text_rect)
        
        controls_text = font.render("WASD - рух | Дійди до правого краю для переходу", True, (255, 255, 255))
        screen.blit(controls_text, (10, HEIGHT - 40))
        
        # Інформація про поточну локацію
        location_text = font.render(f"Локація: {police_background}/3", True, (255, 255, 255))
        screen.blit(location_text, (10, 10))
        
        pygame.display.update()
        clock.tick(60)
        continue
    
    elif game_state == "black_screen":
        screen.fill((0, 0, 0))
        pygame.display.update()
        clock.tick(60)
        continue

    # ---------- МАЛЮВАННЯ ----------
    
    if game_state == "lose":
        screen.fill((0, 0, 0))
        txt = font.render("Натисни R щоб спробувати ще раз", True, (255, 255, 255))
        screen.blit(txt, (WIDTH//2 - 200, HEIGHT//2))
    
    else:
        if game_state in ("collect", "chase"):
            screen.fill((255, 255, 255))
        else:
            screen.blit(battlefield_img, (0, 0))
        
        if game_state == "collect":
            for m in mushrooms:
                screen.blit(mushroom_img, m)
        
        if game_state == "fight":
            screen.blit(dog_fight_img, dog)
        else:
            screen.blit(dog_normal_img, dog)
        
        if game_state == "fight":
            screen.blit(mushroomer_fight_img, mushroomer)
        elif game_state in ("chase", "lose"):
            screen.blit(mushroomer_normal_img, mushroomer)
        
        if game_state == "fight":
            draw_health_bars(dog_health, mushroomer_health, hits_landed)
            control_text = font.render("A/D - рух  |  E - атака", True, (255, 255, 255))
            screen.blit(control_text, (WIDTH//2 - 100, HEIGHT - 40))
            
            if abs(dog.x - mushroomer.x) < 120:
                ready_text = font.render("E", True, (0, 255, 0))
                screen.blit(ready_text, (WIDTH//2 - 10, HEIGHT - 80))
            
            time_since_last = current_time - last_mushroomer_attack_time
            if time_since_last < 1500:
                cooldown_text = font.render(f"{(1500 - time_since_last)//100 + 1}", True, (255, 200, 0))
                screen.blit(cooldown_text, (mushroomer.x + 50, mushroomer.y - 20))

        if game_state == "chase":
            elapsed_sec = (pygame.time.get_ticks() - chase_start) // 1000
            elapsed_sec = min(elapsed_sec, 20)
            txt = font.render(f"{elapsed_sec}/20", True, (0, 0, 0))
            screen.blit(txt, (10, 10))
        
        if game_state in ("collect", "chase"):
            controls_text = font.render("WASD - рух", True, (0, 0, 0))
            screen.blit(controls_text, (10, HEIGHT - 40))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()