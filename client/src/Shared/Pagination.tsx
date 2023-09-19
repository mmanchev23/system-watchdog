const Pagination = ({
    paginationLength,
    currentPage,
    onPageChange,
  }: {
    paginationLength: number;
    currentPage: number;
    onPageChange: (page: number) => void;
  }) => {
    const visiblePageCount = 5;
  
    const getVisiblePages = () => {
      const halfVisible = Math.floor(visiblePageCount / 2);
      const firstVisible = Math.max(1, currentPage - halfVisible);
      const lastVisible = Math.min(paginationLength, firstVisible + visiblePageCount - 1);
      return Array.from({ length: lastVisible - firstVisible + 1 }, (_, i) => firstVisible + i);
    };
  
    return (
      <nav aria-label="Page navigation" className="ml-3">
        <ul className="pagination justify-content-center">
          <li className={`page-item ${currentPage === 1 ? 'disabled' : ''}`}>
            <button
              className="page-link"
              onClick={() => onPageChange(currentPage - 1)}
              disabled={currentPage === 1}
            >
              Previous
            </button>
          </li>
          {getVisiblePages().map((page) => (
            <li key={page} className={`page-item ${currentPage === page && 'active'}`}>
              <button className="page-link" onClick={() => onPageChange(page)}>
                {page}
              </button>
            </li>
          ))}
          <li className={`page-item ${currentPage === paginationLength ? 'disabled' : ''}`}>
            <button
              className="page-link"
              onClick={() => onPageChange(currentPage + 1)}
              disabled={currentPage === paginationLength}
            >
              Next
            </button>
          </li>
        </ul>
      </nav>
    );
};

export default Pagination;
