// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table fato_professor {
  idProfessor integer [primary key]
  nome varchar(45)
  telefone varchar(45)
  cpf varchar(45)
  data_cadastro date
  idDepartamento integer 
  idCurso integer
  idDisciplina integer
  idCampus integer
}

Table dim_departamento {
  idDepartamento integer [primary key]
  nome_departamento varchar(45)
  nome_campus varchar(45)
  idProfessor_coordenador INT
}

Table dim_curso {
  idCurso integer [primary key]
  nome_curso varchar(45)
  data_criacao date
}

Table dim_disciplina {
  idDisciplina integer [primary key]
  nome_disciplina varchar(45)
}

Table dim_tempo {
  data date [primary key]
  mes int
  ano int
}

Table dim_campus {
  idCampus integer [primary key]
  nome varchar(45)
  endereco varchar(45)
  
}

Ref: "dim_tempo"."data" < "fato_professor"."data_cadastro"

Ref: "dim_curso"."idCurso" < "fato_professor"."idCurso"

Ref: "dim_departamento"."idDepartamento" < "fato_professor"."idDepartamento"

Ref: "dim_disciplina"."idDisciplina" < "fato_professor"."idDisciplina"

Ref: "dim_campus"."idCampus" < "fato_professor"."idCampus"

