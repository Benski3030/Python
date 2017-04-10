def lorenzAndGini(x, size=100000):
    '''
    Returns Lorenz curve plot and corresponding gini coefficient.
    
    Parameters:
    -----------
        x: Pandas dataframe object
        size: how many observations should be randomly sampled from the data set
    
    Returns:
    --------
        pandas data frame
    '''
    
    print "Starting process..."
    
    grpData = x[['id', 'total']].groupby('id').sum().sample(size)
    raw_data = np.sort(grpData['total'])
    x = np.linspace(0.0, 1.0, len(raw_data) + 1)
    y_pe = x
    y = [0.0]
    
    print "Arranging data"
    
    for data_point in raw_data:
        y.append(data_point / (np.sum(raw_data)))
    
    y = np.cumsum(y)
    
    print "Calculate the area below the perfect equality line"
    
    area_perfect = np.trapz(y_pe, x)

    print "Compute the area using the composite trapezoidal rule"
    
    area_lorenz = np.trapz(y, x)
    area_lorenz
    
    print "Computing gini coefficient"
    
    # Compute the gini coefficient
    # Divide the difference of 'area_perfect' and 'area_lorenz' by 'area_perfect'
    gini_coeff = (area_perfect - area_lorenz)/area_perfect
    print gini_coeff
    
    # Print gini coefficient (Answer = .19)
    plt.plot(x, y_pe)
    plt.ylim([0,1])
    plt.xlabel("Cumulative % of Population")
    plt.ylabel("Cumulative % of Values")
    plt.plot(x, y)
    plt.title("Lorenz Curve and Gini Index \n %f" %gini_coeff);
