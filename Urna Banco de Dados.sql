create database Urna;
use Urna;

-- Tabela Eleitores ---
create table Eleitores(
id_eleitor int auto_increment primary key,
rm_eleitor int(6) not null unique,
nome_eleitor varchar(60) not null,
sobreN_eleitor varchar(60) not null,
idade_eleitor date not null,
foto_eleitor varchar(120) not null,
curso_eleitor varchar(10) not null
);
select * from Eleitores;

-- Tabela Candidatos ---
create table Candidatos(
id_cand int auto_increment primary key,
id_eleitor int,
nome_cand varchar(60) not null unique,
numero_cand int(2) not null unique,
foto_cand varchar(120) not null,
numerosVotos_cand int,
foreign key (id_eleitor) references Eleitores(id_eleitor)
);

select *from Candidatos;

-- Tabela Votos ---
create table Votos (
id_voto int auto_increment primary key,
id_cand int,
id_eleitor int,
dat_voto date not null,
foreign key (id_eleitor) references Eleitores(id_eleitor),
foreign key (id_cand) references Candidatos(id_cand)
);

select * from Votos;
