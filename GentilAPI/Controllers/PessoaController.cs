using Microsoft.AspNetCore.Mvc;
using System;
using System.Data;
using System.Data.SqlClient;

namespace GentilAPI.Controllers;
    [ApiController]
    [Route("api/[controller]")]
public class PessoasController : ControllerBase
    {
        private readonly string _connectionString;

        public PessoasController()
        {
            // Substitua o valor de _connectionString pelo seu próprio connection string do SQL Server
            _connectionString = "Data Source=localhost;Initial Catalog=gentil_db;User ID=DESKTOP-QQVBDLB\bruno;Password=";
        }

        [HttpGet]
        public IActionResult GetPessoas()
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(_connectionString))
                {
                    connection.Open();

                    using (SqlCommand command = new SqlCommand("NomeDaSuaProcedure", connection))
                    {
                        command.CommandType = CommandType.StoredProcedure;

                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                        {
                            // Obtenha os dados do registro retornado pela procedure
                            int idPessoa = reader.GetInt32(0);
                            string nome = reader.GetString(1);
                            DateTime dataNascimento = reader.GetDateTime(2);
                            decimal salario = reader.GetDecimal(3);
                            string observacoes = reader.GetString(4);

                            // Imprima os dados no console
                            Console.WriteLine($"ID: {idPessoa}, Nome: {nome}, Data de Nascimento: {dataNascimento}, Salário: {salario}, Observações: {observacoes}");
                        }
                    }
                }
            }

            return Ok();
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"An error occurred: {ex.Message}");
        }
    }
}