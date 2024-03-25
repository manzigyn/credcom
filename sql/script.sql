drop table if exists TBConfiguracaoResultado;

create table TBConfiguracaoResultado(
	ConfContratante varchar(50) not null,
	ConfAno int not null,
	ConfMes int not null,
	ConfChave varchar(30) not null default 'status',
	ConfValor varchar(200) not null
);

create index idx_confcontranteAnoMes on TbConfiguracaoResultado (ConfContratante, ConfAno, ConfMes);

create index idx_confAno on TbConfiguracaoResultado (ConfAno);

create index idx_confMes on TbConfiguracaoResultado (ConfMes);

create index idx_confchave on TbConfiguracaoResultado (ConfChave);

drop table if exists TbPagamento ;
CREATE TABLE TbPagamento (
	PagAno int not null,
	PagMes int not null,
	PagContratante VARCHAR(50) not null,
	PagCpfCnpj VARCHAR(20),
	PagNomeCliente VARCHAR(100),
	PagParcelaDataCalculo VARCHAR(300),
	PagTipoNegociacao VARCHAR(100),
	PagVendaQuadraLote VARCHAR(300),
	PagDataAcordo DATE ,
	PagNumeroAcordo INTEGER,
	PagValorHonorarioAcordo DOUBLE,
	PagValorTotalAcordo DOUBLE,
	PagVencimentoParcela DATE,
	PagDataPagamentoParcela DATE,
	PagNossoNumero VARCHAR(100),
	PagNomeCobrador VARCHAR(200),
	PagStatus VARCHAR(100),
	PagEmpreendimento VARCHAR(200),
	PagValorParcela DOUBLE,
	PagValorRecuperado DOUBLE,
	PagArquivoProcessado VARCHAR(100)
);

create index idx_pagano on TbPagamento (PagAno);

create index idx_pagmes on TbPagamento (PagMes);

create index idx_pagcontrante on TbPagamento (PagContratante);

create index idx_pagdataPagamentoParcela on TbPagamento (PagDataPagamentoParcela);

create index idx_pagArquivoProcessado on TbPagamento (PagArquivoProcessado);


drop table if exists TbPagamentoBkp ;
CREATE TABLE TbPagamentoBkp (
	PagAno int not null,
	PagMes int not null,
	PagContratante VARCHAR(100) not null,
	PagCpfCnpj VARCHAR(20),
	PagNomeCliente VARCHAR(100),
	PagParcelaDataCalculo VARCHAR(300),
	PagTipoNegociacao VARCHAR(100),
	PagVendaQuadraLote VARCHAR(300),
	PagDataAcordo DATE ,
	PagNumeroAcordo INTEGER,
	PagValorHonorarioAcordo DOUBLE,
	PagValorTotalAcordo DOUBLE,
	PagVencimentoParcela DATE,
	PagDataPagamentoParcela DATE,
	PagNossoNumero VARCHAR(100),
	PagNomeCobrador VARCHAR(200),
	PagStatus VARCHAR(100),
	PagEmpreendimento VARCHAR(200),
	PagValorParcela DOUBLE,
	PagRecuperado DOUBLE,
	PagArquivoProcessado VARCHAR(100)
);

create index idx_paganoBkp on TbPagamentoBkp (PagAno);

create index idx_pagmesBkp on TbPagamentoBkp (PagMes);

create index idx_pagcontranteBkp on TbPagamentoBkp (PagContratante);

create index idx_pagdataPagamentoParcelaBkp on TbPagamentoBkp (PagDataPagamentoParcela);

create index idx_pagArquivoProcessadoBkp on TbPagamentoBkp (PagArquivoProcessado);


drop table if exists TbDistribuicao;

CREATE TABLE TbDistribuicao (
	DisCarteira VARCHAR(100) not null,
	DisOperador VARCHAR(100),
	DisNumeroParcelas INTEGER,
	DisVenda INTEGER,
	DisUnidade VARCHAR(100),
	DisCodigoClienteContrato INTEGER,
	DisLoteamentoCursoLuc VARCHAR(100),
	DisAtrasoReal VARCHAR(50),
	DisValorTotal DOUBLE,
	DisStatus VARCHAR(150),
	DisCpfCnpj VARCHAR(20),
	DisNome VARCHAR(150),
	DisStatus2 VARCHAR(150),
	DisStatusVirtua VARCHAR(150),
	DisArquivoProcessado VARCHAR(100)
);

create index idx_discarteira on TbDistribuicao (DisCarteira);

create index idx_disstatusVirtua on TbDistribuicao (DisStatusVirtua);


drop table if exists TbDistribuicaoBkp;

CREATE TABLE TbDistribuicaoBkp (
	DisCarteira VARCHAR(100) not null,
	DisOperador VARCHAR(100),
	DisNumeroParcelas INTEGER,
	DisVenda INTEGER,
	DisUnidade VARCHAR(100),
	DisCodigoClienteContrato INTEGER,
	DisLoteamentoCursoLuc VARCHAR(100),
	DisAtrasoReal VARCHAR(50),
	DisValorTotal DOUBLE,
	DisStatus VARCHAR(150),
	DisCpfCnpj VARCHAR(20),
	DisNome VARCHAR(150),
	DisStatus2 VARCHAR(150),
	DisStatusVirtua VARCHAR(150),
	DisArquivoProcessado VARCHAR(100)
);

create index idx_discarteiraBkp on TbDistribuicaoBkp (DisCarteira);

create index idx_disstatusVirtuaBkp on TbDistribuicaoBkp (DisStatusVirtua);

drop table if exists TBParametrizacao;

create table TBParametrizacao(
	ParChave varchar(300) not null,
	ParValor varchar(300)  not null
);

create index idx_parchave on TbParametrizacao (ParChave);

drop table if exists TbLogGeracao;

CREATE TABLE TbLogGeracao (
	GerContratante VARCHAR(100) not null,	
	GerAno int not null,
	GerMes int not null,
	GerOperador VARCHAR(100) not null,
	GerData VARCHAR(10) not null,
	GerHorario VARCHAR(8) not null,
	GerArquivo VARCHAR(100) not null,
	GerCaminho VARCHAR(200) not null
);
create index idx_geranoBkp on TbLogGeracao (GerAno);

create index idx_germesBkp on TbLogGeracao (GerMes);

create index idx_gercontranteBkp on TbLogGeracao (GerContratante);