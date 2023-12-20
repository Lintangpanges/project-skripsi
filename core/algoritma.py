from core.models import *

import random
import time
import math

#melakukan semua proses algoritma
class AG:
  #mendfinisikan atribut yang digunakan
  def __init__(self, waktu, tugas):
    self.num_crommosom = None  # jumlah kromosom awal yang dibangkitkan
    self.waktu = waktu  # data waktu
    self.tugas = tugas  # data tugas
    self.generation = 0  # generasi ke....
    self.max_generation = 2
    self.crommosom = []  # array kromosom sesuai num_cromosom
    self.success = False  # keadaan jika sudah ada solusi terbaik
    self.debug = False  # menampilkan debug jika diset True
    self.fitness = []  # nilai fitness setiap kromosom
    self.console = ""  # menyimpan proses algoritma
    self.total_fitness = 0  # menyimpan total fitness untuk masing-masing kromosom
    self.probability = []  # menyimpan probabilitas fitness masing-masing kromosom
    self.com_pro = []  # menyimpan fitness komulatif untuk masing-masing kromosom
    self.rand = []  # menyimpan bilangan rand()
    self.parent = []  # menyimpan parent saat crossover
    self.best_fitness = 0  # menyimpan nilai fitness tertinggi
    self.best_cromossom = []  # menyimpan kromosom dengan fitness tertinggi
    self.crossover_rate = 75  # prosentase kromosom yang akan dipindah silang
    self.mutation_rate = 25  # prosentase kromosom yang akan dimutasi
    self.time_start = None  # menyimpan waktu mulai proses algoritma
    self.time_end = None  # menyimpan waktu selesai proses algoritma
    
 #untuk melakukan proses generate jadwal
  def generate(self): #menjalankan algo secara keseluruhan
    self.time_start = time.time()
    self.generate_crommosom() #memangil fungsi generate cromosom 

    while self.generation < self.max_generation and not self.success: #memulai proses lopping jika solusi optimal belum tecapai maka proses generasi akan dilakukan hingga mencapai maksimum generasi
      self.generation += 1
      self.console += f"<h6>Generasi ke-{self.generation}</h6>"
      self.show_crommosom() 
      self.calculate_all_fitness() #memangil fungsi hitung total nilai fitness
      self.show_fitness() # memanggil fungsi show fitness

      if not self.success: #jika solusi belum optimal maka dilajutkan ke langkah berikutnya
        self.get_com_pro() #memanggil fungsi perhitungan nilai kumulatif
        self.selection() #melakukan proses seleksi  kromosom
        self.show_crommosom() #menampilkan kromosom hasil seleksi
        self.show_fitness() #memangil fungsi show fitness

      if not self.success: #jika solusi belum optimal maka dilajutkan ke langkah berikutnya
        self.crossover() #melakukan proses crossover
        self.show_crommosom() #menampilkan kromosom hasil crossover
        self.show_fitness() #memangil fungsi show fitness

      if not self.success: #jika solusi belum optimal maka dilajutkan ke langkah berikutnya
        self.mutation() #melakukan proses mutasi
        self.show_crommosom() #menampilkan kromosom hasil mutasi
        self.show_fitness() #memangil fungsi show fitness

    self.save_result() #menyimpan jadwal yang dihasilkan

    self.time_end = time.time()
    execution_time = self.time_end - self.time_start

    data = {
      'best_fitness': self.best_fitness,
      'execution_time': execution_time,
      'generation': self.generation,
      'best_cromossom': self.print_cros(self.best_cromossom),
      'debug': self.get_debug()
    }
    return data

 
  def save_result(self): #menyimpan jadwal yang dihasilkan oleg algo
    Jadwal.objects.all().delete()

    for val in self.best_cromossom:
      jadwal = Jadwal.objects.create(
        tugas= Tugas.objects.get(pk=self.tugas[val['tugas']]['id_tugas']),
        waktu= Hari.objects.get(pk=self.waktu[val['waktu']]['id_hari'])
      )
      jadwal.save()
      
  def get_debug(self): #mengembalikan log proses algortima jika
    if self.debug:
      return "<pre class='border border-1 p-2' style='font-size:0.8em'>{}</pre>".format(self.console)
    return False


#Populasi Awal
  def generate_crommosom(self): #membentuk populasi awal
    numb = 0
    while numb < self.num_crommosom:
      cro = self.get_rand_crommosom()
      self.crommosom.append(cro)
      self.fitness.append(0)
      numb += 1

  def get_rand_crommosom(self):#membangkitkan crosomosom secara random
    result = []
    tugass = self.tugas
    no = 0

    for key, val in tugass.items():
      for a in range(1):
        result.append({'tugas': val['id_tugas'] - 1, 'waktu': random.randint(0, len(self.waktu) - 1), 'color': 'red'})
        no += 1

    return result
  
  def show_crommosom(self):# menampilkan kromosom yang telah di representasikan dari data tugas dan waktu
    cros = self.crommosom
    a = []
    for key, val in enumerate(cros):
      a.append(self.print_cros(val, key))

    self.console += " \r\n".join(a) + "\r\n"

  def print_cros(self, val=[], key=0):
    arr = []
    for v in val:
      arr.append(f"[{v['tugas']}, {v['waktu']}]")
    return "Kromosom[{}]: ({})".format(key, ",".join(arr))
  
  
  #MELAKUKAN PERHITUNGAN NILAI FITNESS
  def get_clash_guru(self, crom): #mendefinisikan fungsi konflik guru dan menghitung konflik guru yang terjadi
    clash = 0
    count = len(crom)

    for a in range(count - 1):
      for b in range(a + 1, count):
        tugas1 = self.tugas[crom[a]['tugas']]
        tugas2 = self.tugas[crom[b]['tugas']]
        if tugas1['id_guru'] == tugas2['id_guru']:
          if crom[a]['waktu'] == crom[b]['waktu']:
            clash += 1
    return clash

  def get_clash_kelas(self, crom): #mendefinisikan fungsi konflik kelas dan menghitung konflik kelas yang terjadi
    clash = 0
    count = len(crom)

    for a in range(count - 1):
      for b in range(a + 1, count):
        tugas1 = self.tugas[crom[a]['tugas']]
        tugas2 = self.tugas[crom[b]['tugas']]
        if tugas1['id_kelas'] == tugas2['id_kelas']:
          if crom[a]['waktu'] == crom[b]['waktu']:
              clash += 1
    return clash
  
  def calculate_fitness(self, key): #menghitung nilai fitness untuk satu kromosom
    cro = self.crommosom[key]
    # guru sama waktu sama
    clash_guru = self.get_clash_guru(cro) #mendefinisikan clash guru sebagai konflik
    # kelas sama waktu sama
    clash_kelas = self.get_clash_kelas(cro) #mendefinisikan clash kelas sebagai konflik

    f = {}
    f['desc'] = f"1/(1+{clash_guru}+{clash_kelas})"
    f['nilai'] = 1 / (1 + clash_guru + clash_kelas)

    if f['nilai'] == 1:  # jika sudah optimal maka berhenti
      self.success = True

    if f['nilai'] > self.best_fitness:
      self.best_fitness = f['nilai']
      self.best_cromossom = self.crommosom[key]

    self.fitness[key] = f
    return f

  def calculate_all_fitness(self): #menghitung nilai fitnes untuk semua kromosom
    for key, val in enumerate(self.crommosom):
      self.calculate_fitness(key)

  def show_fitness(self):  #menampilkan nilai fitness dari semua kromosom yang ada pada populasi
    # print(self.fitness)
    for key, fit in enumerate(self.fitness):
      self.console += f"F[{key}]: {fit['desc']} = {fit['nilai']} \r\n"
    self.get_total_fitness()
    self.console += f"Total F: {self.total_fitness} \r\n"

  def get_total_fitness(self): #menampilkan total nilai fitness dari semua kromosom pada populasi
    self.total_fitness = 0
    for val in self.fitness:
      self.total_fitness += val['nilai']
    return self.total_fitness
  
    
#proses seleksi
  def get_probability(self): # mecari nilai probabilitas dari setiap kromosom
    self.probability = []
    for key, val in enumerate(self.fitness):
      x = val['nilai'] / self.total_fitness
      self.probability.append(x)
    return self.probability

  def get_com_pro(self): #mecari nilai kumulatif dari setiap kromosom
    self.get_probability()

    self.com_pro = []
    x = 0
    for key, val in enumerate(self.probability):
      x += val
      self.com_pro.append(x)
  
  def get_rand(self): #membangkitkan bilangan random
    self.rand = {} #menyimpan bilangan random
    for key, val in enumerate(self.fitness):
      r = random.random()
      self.rand[key] = r
      
  def choose_selection(self, rand_numb=0): #memilih krosomo yang akan diseleksi sesuai dengan nilai kumulatif
    for key, val in enumerate(self.com_pro):
      if rand_numb <= val:
        return key

  def selection(self): # melakukan proses seleksi 
    self.console += "<h6>Seleksi generasi ke-{}</h6>".format(self.generation)
    self.get_rand()
    new_cro = []
    for key, val in self.rand.items():
      k = self.choose_selection(val)
      new_cro.append(self.crommosom[k])
      self.fitness[key] = self.fitness[k]
    self.crommosom = new_cro
    
  
  #Proses Crossover
  def crossover(self): #melakukan proses crossover
    self.console += f"<h6>Pindah silang generasi ke-{self.generation}</h6>"
    parent = [] # berisi cromosom yang di jadikan induk

    for key, val in enumerate(self.crommosom): # memilih cromosom induk
      rnd = random.random() #bangkitkan bilangan random
      if rnd <= self.crossover_rate / 100: # kondisi jika bilangan random lebih kecil atau sama dengan nilai cros maka kromosom akan di jadikan induk
        parent.append(key)

    for key, val in enumerate(parent):
      self.console += f"Parent[{key}]: {val} \r\n"

    c = len(parent) #definisikan panjang atau banyaknya induk 

    if c > 1: #jika induk lebih dari 1 maka akan melakukan proses crossover
      new_cro = {}
      for a in range(c - 1):
        new_cro[parent[a]] = self.get_crossover(parent[a], parent[a + 1])
      new_cro[parent[c - 1]] = self.get_crossover(parent[c - 1], parent[0])

      for key, val in new_cro.items():
        self.crommosom[key] = val
        self.calculate_fitness(key)
  
  def get_crossover(self, key1, key2): # melakukan proses crossover antara kromosom
    cro1 = self.crommosom[key1]
    cro2 = self.crommosom[key2]

    offspring = random.randint(0, len(cro1) - 2) # menghasilkan kromosom anak dengan menyesuaikan titik potong secara acak
    new_cro = [] # kromosom anak baru

    for a in range(len(cro1)):
      if a <= offspring:
        new_cro.append(cro1[a])
      else:
        new_cro.append(cro2[a])

    return new_cro 
  
  #Proses Mutasi
  def mutation(self): #melakukan proses mutasi
    mutation = []
    self.console += f"<h6>Mutasi generasi ke-{self.generation}</h6>"
    gen_per_cro = len(self.tugas) #definisikan jumlah gen pada kromosom 
    total_gen = len(self.crommosom) * gen_per_cro #menghitung panjang gen
    total_mutation = round(self.mutation_rate / 100 * total_gen) #mecari banyak mutasi yang dilakukan

    for _ in range(total_mutation):
      val = random.randint(1, total_gen) # membangkitkan bilangan random sesuai dengan mutasi yang di lakukan

      cro_index = math.ceil(val / gen_per_cro) - 1 #mencari range mutasi
      gen_index = (val - 1) % gen_per_cro

      self.console += f"{val} : [{cro_index}, {gen_index}]\r\n"
      self.crommosom[cro_index][gen_index]['waktu'] = random.randint(0, len(self.waktu) - 1)
      self.fitness[cro_index] = self.calculate_fitness(cro_index)

      if self.success:
        return

    return False