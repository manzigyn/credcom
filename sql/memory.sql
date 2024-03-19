INSTALL spatial;
LOAD spatial;

create table TbPagamento as
select * from st_read('C:\MAF\Magalhaes\credcom\dados\pagamento_01_viverbem.xlsx')

create table TbDistribuicao as
select * from st_read('C:\MAF\Magalhaes\credcom\dados\distribuicao_01_viverbem.xlsx')

select * from tbDistribuicao

drop table if exists TbPagamento ;

create table TbPagamento as
SELECT 
	Contratante 				as PagContratante, 
	"CPF  CNPJ"			    	as PagCpfCnpj,
	"Nome do Cliente" 			as PagNomeCliente,
	"Parcelas e Data Calculo" 	as PagParcelaDataCalculo,
	"Tipo de Negociação" 		as PagTipoNegociacao,
	"Venda - Quadra - Lote" 	as PagVendaQuadraLote,
	"Data Acordo" 				as PagDataAcordo,
	"Nr. Acordo" 				as PagNumeroAcordo,
	"Vlr. Honorário Acordo" 	as PagValorHonorarioAcordo,
	"Vlr. Total Acordo" 		as PagValorTotalAcordo,
	"Dta Vecto Parcela" 		as PagVencimentoParcela,
	"Dta Pgto Parcela"			as PagDataPagamentoParcela,
	"Bol. Nosso Número"			as PagNossoNumero,
	"Nome Cobrador"				as PagNomeCobrador,
	Status						as PagStatus,
	Empreendimento				as PagEmpreendimento,
	"Valor parcela"				as PagValorParcela,
	Recuperado					as PagRecuperado,
	'pagamento_01_viverbem.xlsx'as PagArquivoProcessado
from st_read('C:\MAF\Magalhaes\credcom\dados\pagamento_01_viverbem.xlsx');

select * from tbPagamento

drop table if exists TbDistribuicao; 

create table TbDistribuicao as
SELECT 
	Carteira					as DisCarteira,
	Operador					as DisOperador,
	"Nº Parcelas"				as DisNumeroParcelas,
	Venda						as DisVenda,
	Unidade					as DisUnidade,
	"Cod. Cliente/Contrato"		as DisCodigoClienteContrato,
	"Loteamento/Curso/LUC"		as DisLoteamentoCursoLuc,
	"Atraso real"				as DisAtrasoReal,
	"Valor total"				as DisValorTotal,
	Status						as DisStatus,
	"CPF/CNPJ"					as DisCpfCnpj,
	Nome						as DisNome,
	"Status 2"					as DisStatus2,
	"Status Virtua"				as DisStatusVirtua,
	'distribuicao_01_viverbem.xlsx'as DisArquivoProcessado
from st_read('C:\MAF\Magalhaes\credcom\dados\distribuicao_01_viverbem.xlsx');